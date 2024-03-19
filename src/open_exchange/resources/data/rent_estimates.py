# Standard Library
import concurrent.futures
from typing import TYPE_CHECKING, Iterable

# Third-Party Libraries
import more_itertools

# 1st Party Libraries
from open_exchange.contants import MAX_ADDRESSES_PER_RENT_ESTIMATES_REQUEST, MAX_CONCURRENT_REQUESTS
from open_exchange.resource import APIResource
from open_exchange.types.data import rent_estimates_fetch_params, rent_estimates_response

if TYPE_CHECKING:
    # 1st Party Libraries
    from open_exchange.client import OpenExchangeClient


class RentEstimates(APIResource):
    def __init__(self, client: "OpenExchangeClient") -> None:
        super().__init__(client)
        self._executor = concurrent.futures.ThreadPoolExecutor(max_workers=MAX_CONCURRENT_REQUESTS)

    def fetch(
        self,
        addresses: Iterable[rent_estimates_fetch_params.Address],
        *,
        max_addresses_per_request: int = MAX_ADDRESSES_PER_RENT_ESTIMATES_REQUEST,
    ) -> Iterable[rent_estimates_response.Result]:
        """
        Fetch rent estimates for addresses

        Args:
          addresses: An array of address objects, each specifying a property location.

          max_addresses_per_request: The maximum number of addresses to include in each request.

        Returns:
          An iterable of rent estimates results.
        """
        futures_and_chunk_addresses_tuples = [
            (
                self._executor.submit(
                    self.request,
                    method="POST",
                    path="/data/rent-estimates",
                    body={
                        "addresses": chunk_addresses,
                    },
                ),
                chunk_addresses,
            )
            for chunk_addresses in more_itertools.chunked(addresses, n=max_addresses_per_request)
        ]

        for future, chunk_addresses in futures_and_chunk_addresses_tuples:
            for result_dict in future.result()["results"]:
                yield rent_estimates_response.Result.parse_obj(result_dict)
