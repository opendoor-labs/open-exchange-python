from typing import Iterator

from open_exchange._types import AddressFields, RentalCompsResult


def fetch(addresses: Iterator[AddressFields]) -> Iterator[RentalCompsResult]:
    """
    Fetches rental comps for the given addresses.

    Args:
        addresses: An iterator of address fields.

    Returns:
        An iterator of rental comps results.
    """
    ...
