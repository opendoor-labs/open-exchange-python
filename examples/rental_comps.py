from __future__ import annotations

# 1st Party Libraries
import open_exchange
from open_exchange.types import AddressFields, RentalCompsFilters, RentalCompsResult

# get API KEY from environment variable OPEN_EXCHANGE_API_KEY
client = open_exchange.OpenExchangeClient(base_url='http://localhost:5500/api/v2')

addresses: list[AddressFields] = [
    {
        'street': '1850 NW 37th St',
        'city': 'Oakland Park',
        'state': 'FL',
        'postal_code': '33309',
        'token': 'client-provided-token-1',
    }
]

filters: RentalCompsFilters = {
    'bedrooms_total': {
        'relative': 1,
    }
}

# get rental comps for a iterable of addresses with filters
for result in client.data.rental_comps.fetch(addresses=addresses, filters=filters):  # type: RentalCompsResult
    assert result['token'] == 'client-provided-token-1'

    print('Subject property details:', result['subject_property_details'])
    print('Number of rental comps:', len(result['rental_comps']))
    print('Rental comps:', result['rental_comps'])
