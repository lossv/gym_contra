"""Registration code of Gym environments in this package."""
from .Env.env_contra import ContraEnv
from .Env.env_contra_random_play import ContraRandomStagesEnv
from ._registration import make


# define the outward facing API of this package
__all__ = [
    make.__name__,
    ContraEnv.__name__,
    ContraRandomStagesEnv.__name__,
]
