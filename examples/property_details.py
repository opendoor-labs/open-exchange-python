# Standard Library
from typing import List, Optional

# 1st Party Libraries
import open_exchange
from open_exchange.types.data import property_details_fetch_params, property_details_response

# get API KEY from environment variable OPEN_EXCHANGE_API_KEY
client = open_exchange.OpenExchangeClient()

addresses: List[property_details_fetch_params.Address] = [
    {
        "street": " 5201 S 44th St",
        "city": "Omaha",
        "state": "NE",
        "postal_code": "68107",
        "token": "client-provided-token-1",
    }
]

# get property details for a iterable of addresses
ordered_tokens = [address["token"] for address in addresses]
for result, expected_token in zip(
    client.data.property_details.fetch(addresses=addresses), ordered_tokens
):  # type: (property_details_response.Result, Optional[str])
    assert result.token == expected_token

    if result.property_details:
        print("Subject property details:", result.property_details)
    else:
        print("No property details available for this address.")
