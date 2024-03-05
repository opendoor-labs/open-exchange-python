from __future__ import annotations

# Standard Library
import concurrent.futures
from http import HTTPStatus
from typing import TYPE_CHECKING, Iterable

# Third-Party Libraries
import more_itertools

# 1st Party Libraries
from open_exchange.contants import MAX_ADDRESSES_PER_RENTAL_COMPS_REQUEST, MAX_CONCURRENT_REQUESTS
from open_exchange.resource import APIResource
from open_exchange.types import AddressFields, RentalCompsFilters, RentalCompsResult

if TYPE_CHECKING:
    # 1st Party Libraries
    from open_exchange.client import OpenExchangeClient


class RentalComps(APIResource):
    def __init__(self, client: OpenExchangeClient) -> None:
        super().__init__(client)
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT_REQUESTS)

    def fetch(
        self,
        addresses: Iterable[AddressFields],
        *,
        filters: RentalCompsFilters | None = None,
        num_comps: int | None = 10,
        max_addresses_per_request: int = MAX_ADDRESSES_PER_RENTAL_COMPS_REQUEST,
    ) -> Iterable[RentalCompsResult]:
        """
        Fetches rental comps for the given addresses.

        Args:
            addresses: An iterator of address fields.
            max_addresses_per_request: The maximum number of addresses to include in each request.

        Returns:
            An iterator of rental comps results.
        """
        futures = [
            self._executor.submit(
                self.request,
                method='POST',
                path='/data/rental-comps',
                body={
                    'addresses': chunk_addresses,
                    'filters': filters,
                    'num_comps': num_comps,
                },
            )
            for chunk_addresses in more_itertools.chunked(addresses, n=max_addresses_per_request)
        ]

        for future in concurrent.futures.as_completed(futures):
            for result in future.result()['results']:  # type: RentalCompsResult
                result['api_code'] = self._result_api_code(result)
                yield result

    @staticmethod
    def _result_api_code(result: RentalCompsResult) -> int:
        """
        Returns the API code for the given result.

        TODO: This logic will be moved to the API server in the future.
        """
        if isinstance(result.get('api_code'), int):
            return result['api_code']

        if not result['error_message']:
            return HTTPStatus.OK  # 200 status code

        if result['error_message'] == 'No products found for address':
            # No rental comps found for the address. This is not an error. Billing will not be charged.
            return HTTPStatus.NO_CONTENT  # 204 status code

        if result['error_message'] == 'Could not generate similarity scores':
            # Similarity score dependency is down. Retry later.
            return HTTPStatus.SERVICE_UNAVAILABLE  # 503 status code

        if 'Cannot apply relative filtering on: ' in result['error_message']:
            # Relative filtering is not supported for the given address.
            return HTTPStatus.UNPROCESSABLE_ENTITY  # 422 status code

        # An error occurred.
        return HTTPStatus.INTERNAL_SERVER_ERROR  # 500 status code
