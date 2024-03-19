# Standard Library
import enum
from datetime import date
from typing import Optional, Sequence, Union

# 1st Party Libraries
from open_exchange.typing import TypedDict


class AddressFields(TypedDict, total=False):
    street: str
    """
    The full street address where the property resides, including the street
    number and street name.
    """

    city: str
    """
    The city name where the property resides.
    """

    state: str
    """
    The state abbreviation where the property resides (e.g. `"CA"`).
    """

    postal_code: str
    """
    The 5 digit zip or postal code of the location where the property resides.
    """

    unit: Optional[str]
    """
    The unit type and number of the property (e.g. `"Apt 123"`).
    """

    token: Optional[str]
    """
    A user-defined token to help identify addresses in the response. The token
    which is provided in the request will always be returned in successful
    responses. This token is local to the request and does not persist across
    requests. This field is optional.
    """


class PropertyDetails(TypedDict):
    street: str
    """
    The full street address where the property resides, including the street
    number and street name.
    """

    city: str
    """
    The city name where the property resides.
    """

    state: str
    """
    The state abbreviation where the property resides (e.g. `"CA"`).
    """

    postal_code: str
    """
    The 5 digit zip or postal code of the location where the property resides.
    """

    unit: Optional[str]
    """
    The unit type and number of the property (e.g. `"Apt 123"`).
    """

    latitude: Optional[float]
    """
    The approximate latitude of the property.
    """

    longitude: Optional[float]
    """
    The approximate longitude of the property.
    """

    subdivision_name: Optional[str]
    """
    The name of the subdivision where the property is located.
    """

    bedrooms_total: Optional[int]
    """
    The number of bedrooms, capped at 5.
    """

    bathrooms_full: Optional[int]
    """
    The number of full baths, capped at 5. A full bath contains all 4 of the 4
    elements constituting a bath: Toilet, Sink, Bathtub, or Shower Head. A Full
    Bath will typically contain four elements; Sink, Toilet, Tub, and Shower
    Head (in tub or stall).
    """

    bathrooms_half: Optional[int]
    """
    The number of half baths. A half bath contains a Toilet and a Sink.
    """

    living_area_sqft: Optional[int]
    """
    The approximate livable area within the structure, designated in Square
    Feet.
    """

    above_grade_sqft: Optional[int]
    """
    The living_area_sqft - basement_sqft or `null`.
    """

    lot_size_sqft: Optional[int]
    """
    The total square footage of the lot.
    """

    has_private_pool: Optional[bool]
    """
    TRUE if the property has a privately owned pool that is included in the
    sale/lease.
    """

    basement_sqft: Optional[int]
    """
    The approximate square footage of the basement.
    """

    garage_spaces: Optional[int]
    """
    The number of spaces in the garage(s).
    """

    num_exterior_stories: Optional[int]
    """
    The number of above ground stories on the property.
    """

    year_built: Optional[int]
    """
    The year the property was built, rounded to the nearest 5.
    """

    structure_type: Optional[str]
    """
    The type of structure that the property completely or partially
    encompasses. For example, House or Cabin are the overall structure and
    typically sold or leased as a whole. Multi Family and Docks may be sold
    in whole, but are often sold or leased by unit/slip. This field is the
    type of structure as opposed to style, which is under the Architectural
    Style field.
    """

    hoa: Optional[bool]
    """
    TRUE if the property is inside a hoa. Not set if unknown.
    """

    ownership_profile: Optional[str]
    """
    The property owner's estimated portfolio size. The output can be one of
    the following: "<100", "100-1k", "1k-20k", "20k+".
    """


class RentalComp(TypedDict):
    property_details: PropertyDetails
    """
    The property details for the comp.
    """

    distance_miles: Optional[float]
    """
    The distance in miles from the subject property to the comp.
    """

    is_same_subdivision: Optional[bool]
    """
    TRUE if the comp is in the same subdivision as the subject property.
    """

    initial_list_price_date: Optional[str]
    """
    The approximate first known date at which the listed rent was publicly
    displayed or updated.
    """

    initial_list_price: Optional[int]
    """
    The initial list price of the property.
    """

    last_list_price: Optional[int]
    """
    The approximate last known published list rent for the property,
    denominated in dollars and cents.
    """

    close_price: Optional[int]
    """
    The approximate last known closed monthly rental price for the property,
    denominated in dollars and cents.
    """

    listing_status: Optional[str]
    """
    The status of the property:
    `active` refers to properties that are currently available for rent.
    "closed"` refers to properties that were previously available for rent but
    have since been rented out.
    `removed` indicates that the listing associated with this property is no
    longer active.
    """

    close_price_date: Optional[str]
    """
    The approximate earliest known calendar day on which the closed rent
    became effective.
    """

    count_applications: Optional[int]
    """
    The number of applications received from prospective renters during the
    listing process.
    """

    count_showings: Optional[int]
    """
    The number of times the property was shown to prospective renters during
    the listing process.
    """

    last_event_date: Optional[str]
    """
    The date which the last listing event occurred. This usually means a change
    in `listing_status`.
    """

    last_seen_date: Optional[str]
    """
    The date when the comp was last seen.
    """

    dom: Optional[int]
    """
    Days on Market for this property.
    """

    response_codes: Optional[Sequence[str]]
    """
    A list containing information about this comp subject property pairing.
    The possible response codes are as following:
    - estimated_close_price: the comp’s listing has closed, but the actual
    close price is not yet known. In this case, the last list price is used
    as an estimate. close_price will be equal to the last known list_price
    """

    similarity_score: Optional[float]
    """
    A score between 0 and 1 describing how similar this comp is to the subject
    property. Similarity accounts for both home details (bed, bath, year
    built, etc.) as well as location. A larger score indicates a more similar
    comp.
    """

    move_out_date: Optional[str]
    """
    The date when the tenant moved out from the leased property during the
    previous lease.
    """


class FilterByDateRange(TypedDict):
    min: date
    """
    The minimum date of the range.
    """

    max: date
    """
    The maximum date of the range.
    """


class FilterByNumericRange(TypedDict):
    min: float
    """
    The minimum value of the range.
    """

    max: float
    """
    The maximum value of the range.
    """


class FilterRelativeNumeric(TypedDict):
    relative: float
    """
    The relative value to use for the filter. For example, if the value is `10`,
    the filter will use the value of the subject property and filter by +/- `10`
    of that value.
    """


DateFilterType = Union[FilterByDateRange, FilterRelativeNumeric]
NumericFilterType = Union[FilterByNumericRange, FilterRelativeNumeric]


class ListingStatus(str, enum.Enum):
    ACTIVE = 'active'
    """
    The property is currently available for rent.
    """

    REMOVED = 'removed'
    """
    The listing associated with this property is no longer active.
    """

    CLOSED = 'closed'
    """
    The property was previously available for rent but has since been rented
    out.
    """


class RentalCompsFilters(TypedDict, total=False):
    bedrooms_total: Optional[NumericFilterType]
    """
    When the **`FilterRelativeNumeric`** is used, only comps which have a number
    of bedrooms that are within the provided `value` of the supplied address.
    For example, providing a `value` of `1` for an address that has `2` bedrooms
    will return only comps that have between (inclusive) `2+1 = 3` and `2-1 = 1`
    bedrooms.

    When the **`FilterByNumericRange* is used, only comps with a number of
    bedrooms that fit within the supplied minimum (inclusive) and maximum value
    (inclusive).
    """

    bathrooms_full: Optional[NumericFilterType]
    """
    When the **`FilterRelativeNumeric`** is used, only comps which have a number
    of full bathrooms that are within the provided `value` of the supplied
    address. For example, providing a value of `2` for an address that has `3`
    full bathrooms will return comps that have between (inclusive) `3+2 = 5` and
    `3-2 = 1` full bathrooms.

    When the **`FilterByNumericRange`** is used, only comps with a number of
    full bathrooms that fit within the supplied minimum (inclusive) and maximum
    value (inclusive).
    """

    bathrooms_half: Optional[NumericFilterType]
    """
    When the **`FilterRelativeNumeric`** is used, only comps which have a number
    of half bathrooms that are within the provided `value` of the supplied
    address. For example, providing a value of `1` for an address that has `2`
    half bathrooms will return comps that have between (inclusive) `2+1 = 3`
    and `2-1 = 1` half bathrooms.

    When the **`FilterByNumericRange`** is used, only comps with a number of
    half bathrooms that fit within the supplied minimum (inclusive) and maximum
    value (inclusive).
    """

    distance: Optional[float]
    """
    The maximum distance of the rental comp from the requested address. If no
    distance filter was provided, a default value of 2 will be used. This
    distance value provided must be greater than 0 and less than or equal to 25.
    """

    min_similarity_score: Optional[float]
    """
    Lower bound for the similarity score filter for nearby properties to be
    considered as comps. Float within the range from 0 (Least similar) to 1
    (Most similar).
    """

    living_area_sqft: Optional[NumericFilterType]
    """
    When the **`FilterRelativeNumeric`** is used, only comps which have a square
    footage that is within the provided percentage `value` of the supplied
    address. For example, providing a value of `20` for an address that has
    `2500` square feet will return comps that have between (inclusive) `3000`
    and `2000` square feet as we look at +/- `20%` of the subject property
    square footage.

    When the **`FilterByNumericRange`** is used, only comps with a square
    footage that fits within the supplied minimum (inclusive) and maximum value
    (inclusive).
    """

    date: Optional[DateFilterType]
    """
    When the **`FilterRelativeNumeric`** is used, only comps which have a
    `year_built` within provided `value` years of the supplied address. For
    example, providing a value of `2` for an address that was built in `2019`
    square feet will return comps that were built between `2017` and `2021` as
    we look at +/- `2` years of the subject address.

    When the **`FilterByNumericRange`** is used, only comps built within the
    supplied minimum (inclusive) and maximum value (inclusive) years will be
    returned.
    """

    year_built: Optional[NumericFilterType]
    """
    When the **`FilterRelativeNumeric`** is used, only comps which have a
    `year_built` within provided `value` years of the supplied address. For
    example, providing a value of `2` for an address that was built in `2019`
    square feet will return comps that were built between `2017` and `2021` as
    we look at +/- `2` years of the subject address.

    When the **`FilterByNumericRange`** is used, only comps built within the
    supplied minimum (inclusive) and maximum value (inclusive) years will be
    returned.
    """

    statuses: Sequence[ListingStatus]
    """
    Only comps with statuses that match at least one of the statuses within the
    list supplied will be returned.
    """


class RentalCompsResult(TypedDict):
    subject_property_details: Optional[PropertyDetails]
    """
    The property details for the address.
    """

    rental_comps: Sequence[RentalComp]
    """
    A list of rental comps for the subject property.
    """

    error_message: Optional[str]
    """
    If an error occurred while processing the request, this field will contain
    a message describing the error. This field is optional.
    """

    api_code: int
    """
    An HTTP status code indicating the result of the address request.
    """

    token: Optional[str]
    """
    The user-supplied token submitted for the address.
    """
