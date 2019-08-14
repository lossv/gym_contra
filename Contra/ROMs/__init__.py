"""Methods for ROM file management."""
from .decode_target import decode_target


# explicitly define the outward facing API of this package
__all__ = [
    decode_target.__name__,
]
