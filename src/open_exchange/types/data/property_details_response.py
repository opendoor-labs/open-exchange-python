# Standard Library
from typing import List, Optional

# 1st Party Libraries
from open_exchange.types.models import BaseModel

__all__ = ["PropertyDetailsResponse", "Result", "ResultPropertyDetails"]


class ResultPropertyDetails(BaseModel):
    city: str
    """The city name where the property resides."""

    postal_code: str
    """The 5 digit zip or postal code of the location where the property resides."""

    state: str
    """The state abbreviation where the property resides (e.g. `"CA"`)."""

    street: str
    """
    The full street address where the property resides, including the street number
    and street name.
    """

    above_grade_sqft: Optional[int] = None
    """The living_area_sqft - basement_sqft or `null`"""

    basement_sqft: Optional[int] = None
    """The approximate square footage of the basement."""

    bathrooms_full: Optional[int] = None
    """The number of full baths, capped at 5.

    A full bath contains all 4 of the 4 elements constituting a bath: Toilet, Sink,
    Bathtub, or Shower Head. A Full Bath will typically contain four elements; Sink,
    Toilet, Tub, and Shower Head (in tub or stall).
    """

    bathrooms_half: Optional[int] = None
    """The number of half baths. A half bath contains a Toilet and a Sink"""

    bedrooms_total: Optional[int] = None
    """The number of bedrooms, capped at 5."""

    garage_spaces: Optional[int] = None
    """The number of spaces in the garage(s)."""

    has_private_pool: Optional[bool] = None
    """
    TRUE if the property has a privately owned pool that is included in the
    sale/lease.
    """

    is_in_hoa: Optional[bool] = None
    """TRUE if the property is inside a hoa. Not set if unknown."""

    latitude: Optional[float] = None
    """The approximate latitude of the property."""

    living_area_sqft: Optional[int] = None
    """The approximate livable area within the structure, designated in Square Feet."""

    longitude: Optional[float] = None
    """The approximate longitude of the property."""

    lot_size_sqft: Optional[int] = None
    """The total square footage of the lot."""

    num_exterior_stories: Optional[int] = None
    """The number of above ground stories on the property."""

    ownership_profile: Optional[str] = None
    """The property owner's estimated portfolio size.

    The output can be one of the following: "<100", "100-1k", "1k-20k", "20k+".
    """

    slug: Optional[str] = None
    """A URL-safe string identifying the property address.

    The slug may be used in Rental Advisor URLs (e.g.
    https://rentaladvisor.opendoor.com/address/{slug}).
    """

    structure_type: Optional[str] = None
    """The type of structure that the property completely or partially encompasses.

    For example, House or Cabin are the overall structure and typically sold or
    leased as a whole. Multi Family and Docks may be sold in whole, but are often
    sold or leased by unit/slip. This field is the type of structure as opposed to
    style, which is under the Architectural Style field.
    """

    subdivision_name: Optional[str] = None
    """The name of the subdivision where the property is located."""

    unit: Optional[str] = None
    """The unit type and number of the property (e.g. `"Apt 123"`)."""

    year_built: Optional[int] = None
    """The year the property was built, rounded to the nearest 5."""


class Result(BaseModel):
    token: Optional[str] = None
    """The user-supplied token submitted for the address."""

    error_message: Optional[str] = None
    """The error message if the system was unable to process this address."""

    property_details: Optional[ResultPropertyDetails] = None
    """The property details for the given address."""


class PropertyDetailsResponse(BaseModel):
    results: List[Result]
