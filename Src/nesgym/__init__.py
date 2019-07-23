import os
from gym.envs.registration import register
from .nesenv import NESEnv
from .Contra_env import Contra_env
from .wrappers import wrap_nes_env

register(
    id='ContraGym-v0',
    entry_point='nesgym:Contra_env',
    max_episode_steps=9999999,
    reward_threshold=32000,
    kwargs={},
    nondeterministic=True,
)
