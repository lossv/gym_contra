"""Registration code of Gym environments in this package."""
import gym


def _register_Contra_env(Name):
    """
    Register a Contra. (1/2) stage environment with OpenAI Gym.

    Args:
        Name (str): id for the env to register

    Returns:
        None

    """
    # register the environment
    # gym.envs.registration.register(
    #     id=Name,
    #     entry_point='env_contra:ContraEnv',
    #     max_episode_steps=9999999,
    #     reward_threshold=32000,
    #     kwargs={},
    #     nondeterministic=True
    # )

    gym.envs.registration.register(
        id=Name,
        entry_point='Contra.env_contra:ContraEnv',
        max_episode_steps=9999999,
        reward_threshold=32000,
        kwargs={},
        nondeterministic=True
    )


_register_Contra_env("Contra-v0")

# create an alias to gym.make for ease of access
make = gym.make

# define the outward facing API of this module (none, gym provides the API)
__all__ = [make.__name__]
