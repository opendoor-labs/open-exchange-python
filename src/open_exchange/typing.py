import sys

if sys.version_info >= (3, 8):
    # TypedDict is available in Python 3.8+
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = [
    'TypedDict',
]
