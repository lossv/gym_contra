# import retro
# text = str(retro.data.list_games())
# print(text)
# with open("list.txt", "w+") as f:
#     f.write(text)

import retro

try:
    from mpi4py import MPI
except ImportError:
    MPI = None

import tensorflow as tf
import baselines.ppo2.ppo2 as ppo2
from baselines.common.atari_wrappers import *
# from baselines.common.retro_wrappers import *
from baselines import bench
from baselines.common.vec_env.subproc_vec_env import SubprocVecEnv
from baselines.common.vec_env.dummy_vec_env import DummyVecEnv
from baselines.common import set_global_seeds
import time
import retro
import gym
# from baselines.common.models import register
# from baselines.a2c import utils
# from baselines.a2c.utils import conv, fc, conv_to_fc, batch_to_seq, seq_to_batch
import numpy as np
import argparse
import os
from baselines import logger


def main():
    # # env = retro.make(game='ContraForce-Nes')
    # env = retro.make('ContraIII-Snes')
    # # Airstriker - Genesis
    # obs = env.reset()
    # while True:
    #     obs, rew, done, info = env.step(env.action_space.sample())
    #     env.render()
    #     if done:
    #         obs = env.reset()
    # env.close()

    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--num_env', default=1, type=int)
    parser.add_argument('--seed', default=None, type=int)
    parser.add_argument('--game', default='ContraIII-Snes')
    parser.add_argument('--state', default='level1.1player.easy.100lives')  # state=retro.State.DEFAULT
    parser.add_argument('--scenario', default='scenario')
    parser.add_argument('--discrete_actions', default=0, type=int)
    parser.add_argument('--bk2dir', default='videos')
    parser.add_argument('--monitordir', default='logs')
    parser.add_argument('--sonic_discretizer', default=1, type=int)
    parser.add_argument('--clip_rewards', default=0, type=int)
    parser.add_argument('--stack', default=4, type=int)
    parser.add_argument('--time_limit', default=8000, type=int)
    parser.add_argument('--scale_reward', default=0.01, type=float)
    parser.add_argument('--warp_frame', default=1, type=int)
    parser.add_argument('--stochastic_frame_skip', default=4, type=int)
    parser.add_argument('--skip_prob', default=0.0, type=float)
    parser.add_argument('--network', default='cnn')
    parser.add_argument('--scenario_number', default=1, type=int)
    parser.add_argument('--load_path', default=None)
    args = parser.parse_args()
    time_int = int(time.time())

    env_vec = make_vec_env(args, time_int)


def make_vec_env(args, time_int, start_index=0):
    """
    Create a wrapped, monitored SubprocVecEnv
    """
    mpi_rank = MPI.COMM_WORLD.Get_rank() if MPI else 0
    seed = args.seed + 10000 * mpi_rank if args.seed is not None else None


    # set_global_seeds(seed)
    # if args.num_env > 1:
    #     return SubprocVecEnv([make_thunk(i + start_index) for i in range(args.num_env)])
    # else:
    #     return DummyVecEnv([make_thunk(start_index)])


def make_env(game='ContraIII-Snes', state='level1.1player.easy.100lives',
             scenario='scenario', discrete_actions=False,
             scenario_number=1):
    use_restricted_actions = retro.Actions.FILTERED  # retro.ACTIONS_FILTERED
    if discrete_actions:
        use_restricted_actions = retro.Actions.DISCRETE  # retro.ACTIONS_DISCRETE

    print("scenario is {}".format(scenario))
    if scenario_number <= 1:
        env = retro.make(game, state, scenario=scenario, use_restricted_actions=use_restricted_actions)
    else:
        scenario = scenario + "_{}".format(subrank % scenario_number)
        env = retro.make(game, state, scenario=scenario, use_restricted_actions=use_restricted_actions)
    obs = env.reset()
    while True:
        obs, rew, done, info = env.step(env.action_space.sample())
        env.render()
        if done:
            obs = env.reset()


if __name__ == "__main__":
    make_env()
