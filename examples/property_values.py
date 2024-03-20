# Standard Library
from typing import List, Optional

# 1st Party Libraries
import open_exchange
from open_exchange.types.data import property_values_fetch_params, property_values_response

# get API KEY from environment variable OPEN_EXCHANGE_API_KEY
client = open_exchange.OpenExchangeClient()

addresses: List[property_values_fetch_params.Address] = [
    {
        "street": " 5201 S 44th St",
        "city": "Omaha",
        "state": "NE",
        "postal_code": "68107",
        "token": "client-provided-token-1",
    }
]

# get property values for a iterable of addresses
ordered_tokens = [address["token"] for address in addresses]
for result, expected_token in zip(
    client.data.property_values.fetch(addresses=addresses), ordered_tokens
):  # type: (property_values_response.Result, Optional[str])
    assert result.token == expected_token

    print("Token:", result.token)
    if result.property_value:
        print("Property value low:", result.property_value.value_low)
        print("Property value:", result.property_value.value)
        print("Property value high:", result.property_value.value_high)
    else:
        print("No property value available for this address")
