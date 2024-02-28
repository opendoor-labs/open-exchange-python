from typing import Iterator

from src.ox_data_api._types import AddressFields, RentalCompsResult


def fetch(addresses: Iterator[AddressFields]) -> Iterator[RentalCompsResult]:
    """
    Fetches rental comps for the given addresses.

    Args:
        addresses: An iterator of address fields.

    Returns:
        An iterator of rental comps results.
    """
    ...
