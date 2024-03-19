# Standard Library
import concurrent.futures
from http import HTTPStatus
from typing import TYPE_CHECKING, Dict, Iterable, List, Optional

# Third-Party Libraries
import more_itertools

# 1st Party Libraries
from open_exchange.contants import (
    DEFAULT_RETRYABLE_STATUS_CODES,
    MAX_ADDRESSES_PER_RENTAL_COMPS_REQUEST,
    MAX_CONCURRENT_REQUESTS,
)
from open_exchange.resource import APIResource
from open_exchange.types.data import rental_comps_fetch_params, rental_comps_response

if TYPE_CHECKING:
    # 1st Party Libraries
    from open_exchange.client import OpenExchangeClient


class RentalComps(APIResource):
    def __init__(self, client: "OpenExchangeClient") -> None:
        super().__init__(client)
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT_REQUESTS)

    def fetch(
        self,
        addresses: Iterable[rental_comps_fetch_params.Address],
        *,
        filters: Optional[rental_comps_fetch_params.Filters] = None,
        num_comps: Optional[int] = 10,
        max_addresses_per_request: int = MAX_ADDRESSES_PER_RENTAL_COMPS_REQUEST,
    ) -> Iterable[rental_comps_response.Result]:
        """
        Fetch rental comps for addresses

        Args:
          addresses: An array of address objects, each specifying a property location.

          filters: An _optional_ object containing criteria to refine the rental comps search, such
              as date range, price, number of bedrooms, etc. If no filters are provided, the
              search will include all available comps.

          num_comps: An _optional_ int containing the number of rental comps to return per subject
              address. The minimum value is 1 and the maximum value is 50. If no value is
              provided, we will return our top 10 comps.

          max_addresses_per_request: The maximum number of addresses to include in each request.

        Returns:
            An iterator of rental comps results.
        """
        futures_and_chunk_addresses_tuples = [
            (
                self._executor.submit(
                    self.request,
                    method="POST",
                    path="/data/rental-comps",
                    body={
                        "addresses": chunk_addresses,
                        "filters": filters,
                        "num_comps": num_comps,
                    },
                ),
                chunk_addresses,
            )
            for chunk_addresses in more_itertools.chunked(addresses, n=max_addresses_per_request)
        ]

        for future, chunk_addresses in futures_and_chunk_addresses_tuples:
            results = _results_from_response(future.result())

            # Retry any failed addresses from the chunk.
            if any(result.api_code in DEFAULT_RETRYABLE_STATUS_CODES for result in results):
                retry_addresses: List[rental_comps_fetch_params.Address] = []
                retry_indices: List[int] = []
                for idx, (result, address) in enumerate(zip(results, chunk_addresses)):
                    if result.api_code not in DEFAULT_RETRYABLE_STATUS_CODES:
                        continue
                    retry_addresses.append(address)
                    retry_indices.append(idx)
                retry_results = _results_from_response(
                    self.request(
                        method="POST",
                        path="/data/rental-comps",
                        body={
                            "addresses": retry_addresses,
                            "filters": filters,
                            "num_comps": num_comps,
                        },
                    )
                )
                for idx, result in zip(retry_indices, retry_results):
                    results[idx] = result  # Replace the failed result with the retry result.

            yield from results


def _results_from_response(response: dict) -> List[rental_comps_response.Result]:
    result_dicts: List[Dict] = response["results"]

    results: List[rental_comps_response.Result] = []
    for result_dict in result_dicts:
        result = rental_comps_response.Result.parse_obj(result_dict)
        result.api_code = _result_api_code(result)
        results.append(result)

    return results


def _result_api_code(result: rental_comps_response.Result) -> int:
    """
    Returns the API code for the given result.

    TODO: This logic will be moved to the API server in the future.
    """
    if isinstance(result.api_code, int):
        return result.api_code

    if not result.error_message:
        return HTTPStatus.OK  # 200 status code

    if result.error_message == "No products found for address":
        # No rental comps found for the address. This is not an error. Billing will not be charged.
        return HTTPStatus.NO_CONTENT  # 204 status code

    if result.error_message == "Could not generate similarity scores":
        # Similarity score dependency is down. Retry later.
        return HTTPStatus.SERVICE_UNAVAILABLE  # 503 status code

    if "Cannot apply relative filtering on: " in result.error_message:
        # Relative filtering is not supported for the given address.
        return HTTPStatus.UNPROCESSABLE_ENTITY  # 422 status code

    # An error occurred.
    return HTTPStatus.INTERNAL_SERVER_ERROR  # 500 status code
