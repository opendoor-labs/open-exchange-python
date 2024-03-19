try:
    # Standard Library
    from functools import cached_property  # type: ignore
except ImportError:
    # Third-Party Libraries
    from cached_property import cached_property

__all__ = [
    "cached_property",
]
