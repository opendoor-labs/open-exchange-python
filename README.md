# Open Exchange Python SDK

The Open Exchange Python SDK provides access to the Open Exchange REST API from applications written in Python 3.6
and later.

## Documentation

The REST API documentation is available at [https://openexchange.readme.io/](https://openexchange.readme.io/).

## Installation

You can install the package via pip:

```bash
pip install open-exchange
```

## Usage

See the [examples][0] directory for examples of how to use the SDK.

```python
import open_exchange
from open_exchange.types.data import rental_comps_fetch_params, rental_comps_response
from typing import List

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
result: rental_comps_response.Result
for result in client.data.rental_comps.fetch(addresses=addresses, filters=filters):
    assert result.token == "client-provided-token-1"

    print("Subject property details:", result.subject_property_details)
    print("Number of rental comps:", len(result.rental_comps))
    print("Rental comps:", result.rental_comps)
```

## Logging

We use the Python standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

## Requirements

Python 3.6 or higher.


[0]: https://github.com/opendoor-labs/open-exchange-python/tree/main/examples