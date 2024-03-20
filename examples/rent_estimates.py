# Standard Library
from typing import List, Optional

# 1st Party Libraries
import open_exchange
from open_exchange.types.data import rent_estimates_fetch_params, rent_estimates_response

# get API KEY from environment variable OPEN_EXCHANGE_API_KEY
client = open_exchange.OpenExchangeClient()

addresses: List[rent_estimates_fetch_params.Address] = [
    {
        "street": " 5201 S 44th St",
        "city": "Omaha",
        "state": "NE",
        "postal_code": "68107",
        "token": "client-provided-token-1",
    }
]

# get rent estimates for the addresses
ordered_tokens = [address["token"] for address in addresses]
for result, expected_token in zip(
    client.data.rent_estimates.fetch(addresses=addresses), ordered_tokens
):  # type: (rent_estimates_response.Result, Optional[str])
    assert result.token == expected_token

    print("Token:", result.token)
    if result.rent_estimate:
        print("Estimated Rent Low:", result.rent_estimate.estimated_rent_low)
        print("Estimated Rent:", result.rent_estimate.estimated_rent)
        print("Estimated Rent High:", result.rent_estimate.estimated_rent_high)
    else:
        print("No rent estimate available for this address")
