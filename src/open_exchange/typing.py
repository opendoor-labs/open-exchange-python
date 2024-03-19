# Standard Library
import sys

if sys.version_info >= (3, 8):
    # TypedDict is available in Python 3.8+
    # Standard Library
    from typing import TypedDict
else:
    # Third-Party Libraries
    from typing_extensions import TypedDict

__all__ = [
    "TypedDict",
]
