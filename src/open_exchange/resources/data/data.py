from __future__ import annotations

# 1st Party Libraries
from open_exchange.compat import cached_property
from open_exchange.resource import APIResource
from open_exchange.resources.data.rental_comps import RentalComps


class Data(APIResource):
    @cached_property
    def rental_comps(self) -> RentalComps:
        return RentalComps(client=self.client)
