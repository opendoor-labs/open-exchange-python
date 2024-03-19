# Standard Library
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    # 1st Party Libraries
    from open_exchange.client import OpenExchangeClient


class APIResource:
    client: "OpenExchangeClient"

    def __init__(self, client: "OpenExchangeClient") -> None:
        self.client = client
        self.request = client._request
