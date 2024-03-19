# 1st Party Libraries
from open_exchange.compat import cached_property
from open_exchange.resource import APIResource
from open_exchange.resources.data.property_details import PropertyDetails
from open_exchange.resources.data.property_values import PropertyValues
from open_exchange.resources.data.rent_estimates import RentEstimates
from open_exchange.resources.data.rental_comps import RentalComps


class Data(APIResource):
    @cached_property
    def property_details(self) -> PropertyDetails:
        return PropertyDetails(client=self.client)

    @cached_property
    def property_values(self) -> PropertyValues:
        return PropertyValues(client=self.client)

    @cached_property
    def rent_estimates(self) -> RentEstimates:
        return RentEstimates(client=self.client)

    @cached_property
    def rental_comps(self) -> RentalComps:
        return RentalComps(client=self.client)
