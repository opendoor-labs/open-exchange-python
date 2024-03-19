# Standard Library
from typing import List, Optional

# 1st Party Libraries
from open_exchange.types.models import BaseModel

__all__ = ["PropertyValuesResponse", "Result", "ResultPropertyValue"]


class ResultPropertyValue(BaseModel):
    value: int
    """The automated valuation model (AVM) mean for the address."""

    value_high: int
    """The upper bound of the automated valuation model (AVM) range."""

    value_low: int
    """The lower bound of the automated valuation model (AVM) range."""


class Result(BaseModel):
    token: Optional[str] = None
    """The user-supplied token submitted for the address."""

    error_message: Optional[str] = None
    """The error message if the system was unable to process this address."""

    property_value: Optional[ResultPropertyValue] = None
    """The property value for the address."""


class PropertyValuesResponse(BaseModel):
    results: List[Result]
    """The list of property values, one for each address."""
