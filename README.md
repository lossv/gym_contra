# gym_contra
A gym game for Contra that for reinforcement learning for Python3.6 or Later

start random play with Src/ttt.py 

![image](https://github.com/OuYanghaoyue/gym_contra/blob/master/Img/TIM%E5%9B%BE%E7%89%8720190723143124.png)


# Gym for Contra

An [OpenAI](https://github.com/openai/gym) Gym environment for Contra.  on The Nintendo Entertainment System (NES) using the [nes-py emulator](https://github.com/Kautenja/nes-py).

# Installation
---

The preferred installation of env is from pip:

```
git clone git@github.com:OuYanghaoyue/gym_contra.git
```
<font color="#dd00dd">Contra-v0</font>

# Usage
## Python
You must import <font color="#dd00dd">ContraEnv</font> before trying to make an environment. This is because gym environments are registered at runtime. By default, <font color="#dd00dd">ContraEnv</font> use the full NES action space of 256 discrete actions. To contstrain this, <font color="#dd00dd">ContraEnv</font>.actions provides three actions lists (RIGHT_ONLY, SIMPLE_MOVEMENT, and COMPLEX_MOVEMENT) for the nes_py.wrappers.JoypadSpace wrapper. See [Env/actions.py](https://github.com/OuYanghaoyue/gym_contra/blob/master/Src/Env/actions.py) for a breakdown of the legal actions in each of these three lists.


```
from nes_py.wrappers import JoypadSpace
from Src.Env.actions import SIMPLE_MOVEMENT, COMPLEX_MOVEMENT
import gym

env = gym.make('Contra-v0')
env = JoypadSpace(env, COMPLEX_MOVEMENT)


done = True
for step in range(5000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(env.action_space.sample())
    env.render()

env.close()

```

> NOTE: ContraEnv.make is just an alias to gym.make for convenience.
> 
> NOTE: remove calls to render in training code for a nontrivial speedup.

## Command Line
<font color="#dd00dd">ContraEnv</font> features a command line interface for playing environments using either the keyboard, or uniform random movement.


```
ContraEnv -m <`human` or `random`>
```
<font color="#FF69B4"> </font>

> NOTE: by default,-m is set to human.

## Environments
These environments allow 3 attempts (lives) to play in the game. The environments only send <font color="#FF69B4">reward-able game-play </font> frames to agents; No cut-scenes, loading screens, etc. are sent from the NES emulator to an <font color="#FF69B4">agent</font> nor can an agent perform actions during these instances. If a cut-scene is not able to be skipped by hacking the NES's RAM, the environment will lock the Python process until the emulator is ready for the next action.

```
