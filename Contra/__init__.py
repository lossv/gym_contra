"""Registration code of Gym environments in this package."""
from .env_contra import ContraEnv
from ._registration import make


# define the outward facing API of this package
__all__ = [
    make.__name__,
    ContraEnv.__name__,
]
