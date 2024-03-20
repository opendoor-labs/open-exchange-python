# Standard Library
from typing import List, Optional

# 1st Party Libraries
import open_exchange
from open_exchange.types.data import rental_comps_fetch_params, rental_comps_response

# get API KEY from environment variable OPEN_EXCHANGE_API_KEY
client = open_exchange.OpenExchangeClient()

addresses: List[rental_comps_fetch_params.Address] = [
    {
        "street": " 5201 S 44th St",
        "city": "Omaha",
        "state": "NE",
        "postal_code": "68107",
        "token": "client-provided-token-1",
    }
]

filters: rental_comps_fetch_params.Filters = {
    "bedrooms_total": {
        "relative": 1,
    }
}

# get rental comps for a iterable of addresses with filters
ordered_tokens = [address["token"] for address in addresses]
for result, expected_token in zip(
    client.data.rental_comps.fetch(addresses=addresses, filters=filters), ordered_tokens
):  # type: (rental_comps_response.Result, Optional[str])
    assert result.token == expected_token

    print("Subject property details:", result.subject_property_details)
    print("Number of rental comps:", len(result.rental_comps))

    if len(result.rental_comps) > 0:
        print("Rental comps:", result.rental_comps)
    else:
        print("No rental comps available for this address.")
