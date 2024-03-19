# Standard Library
from typing import List

# 1st Party Libraries
import open_exchange
from open_exchange.types.data import rental_comps_fetch_params

# get API KEY from environment variable OPEN_EXCHANGE_API_KEY
client = open_exchange.OpenExchangeClient()

addresses: List[rental_comps_fetch_params.Address] = [
    {
        "street": "1850 NW 37th St",
        "city": "Oakland Park",
        "state": "FL",
        "postal_code": "33309",
        "token": "client-provided-token-1",
    },
    {
        "street": "1868 Colin Creek Ln",
        "city": "Charlotte",
        "state": "NC",
        "postal_code": "28214",
        "token": "client-provided-token-2",
    },
    {
        "street": "331 Estelle Dr",
        "city": "Lexington",
        "state": "NC",
        "postal_code": "27295",
        "token": "client-provided-token-3",
    },
    {
        "street": "937 Cassidy Dr",
        "city": "Gastonia",
        "state": "NC",
        "postal_code": "28054",
        "token": "client-provided-token-4",
    },
    {
        "street": "4885 Montcalm Dr SW",
        "city": "Atlanta",
        "state": "GA",
        "postal_code": "30331",
        "token": "client-provided-token-5",
    },
    {
        "street": "3378 Carducci Dr",
        "city": "Converse",
        "state": "TX",
        "postal_code": "78109",
        "token": "client-provided-token-6",
    },
    {
        "street": "459 Fernwood Cir",
        "city": "Statham",
        "state": "GA",
        "postal_code": "30666",
        "token": "client-provided-token-7",
    },
    {
        "street": "1088 Travis St SW",
        "city": "Marietta",
        "state": "GA",
        "postal_code": "30060",
        "token": "client-provided-token-8",
    },
    {
        "street": "2977 Jenkins Dr",
        "city": "Snellville",
        "state": "GA",
        "postal_code": "30078",
        "token": "client-provided-token-9",
    },
    {
        "street": "945 S Willhaven Dr",
        "city": "Fuquay Varina",
        "state": "NC",
        "postal_code": "27526",
        "token": "client-provided-token-10",
    },
    {
        "street": "6747 Arid Way",
        "city": "San Antonio",
        "state": "TX",
        "postal_code": "78252",
        "token": "client-provided-token-11",
    },
    {
        "street": "169 Freedom Dr",
        "city": "Dallas",
        "state": "GA",
        "postal_code": "30157",
        "token": "client-provided-token-12",
    },
    {
        "street": "1414 Pueblo",
        "city": "Denver",
        "state": "NC",
        "postal_code": "28037",
        "token": "client-provided-token-13",
    },
    {
        "street": "1238 Cabots Dr",
        "city": "Auburn",
        "state": "GA",
        "postal_code": "30011",
        "token": "client-provided-token-14",
    },
    {
        "street": "13003 Rosemary Cv",
        "city": "Saint Hedwig",
        "state": "TX",
        "postal_code": "78109",
        "token": "client-provided-token-15",
    },
    {
        "street": "8902 Arbor Creek Dr",
        "city": "Charlotte",
        "state": "NC",
        "postal_code": "28269",
        "token": "client-provided-token-16",
    },
    {
        "street": "3815 Streamside Dr",
        "city": "Gastonia",
        "state": "NC",
        "postal_code": "28056",
        "token": "client-provided-token-17",
    },
    {
        "street": "19120 Cicerone Ct",
        "city": "New Caney",
        "state": "TX",
        "postal_code": "77357",
        "token": "client-provided-token-18",
    },
    {
        "street": "14765 Country Club Dr",
        "city": "Beaumont",
        "state": "TX",
        "postal_code": "77705",
        "token": "client-provided-token-19",
    },
    {
        "street": "11611 Valley Gdn",
        "city": "San Antonio",
        "state": "TX",
        "postal_code": "78245",
        "token": "client-provided-token-20",
    },
    {
        "street": "3110 Persing Ct",
        "city": "Monroe",
        "state": "NC",
        "postal_code": "28110",
        "token": "client-provided-token-21",
    },
]

filters: rental_comps_fetch_params.Filters = {
    "bedrooms_total": {
        "relative": 1,
    }
}

# get rental comps for a iterable of addresses with filters
ordered_tokens = [address["token"] for address in addresses]
for result, expected_token in zip(client.data.rental_comps.fetch(addresses=addresses, filters=filters), ordered_tokens):
    assert result.token == expected_token

    print("Subject property details:", result.subject_property_details)
    print("Number of rental comps:", len(result.rental_comps))

    if len(result.rental_comps) > 0:
        print("Rental comps:", result.rental_comps)
    else:
        print("No rental comps available for this address.")
