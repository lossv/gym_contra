# gym_contra
A gym game for Contra that for reinforcement learning for Python3.6 or Later

start random play with Src/ttt.py 

![image](https://github.com/OuYanghaoyue/gym_contra/blob/master/Img/TIM%E5%9B%BE%E7%89%8720190723143124.png)


# Gym for Contra

An [OpenAI](https://github.com/openai/gym) Gym environment for Contra.  on The Nintendo Entertainment System (NES) using the [nes-py emulator](https://github.com/Kautenja/nes-py).

# Installation
---

The preferred installation of env is from git clone:

```
git clone git@github.com:OuYanghaoyue/gym_contra.git
```

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

## Step
> Info about the rewards and info returned by the step method.

### Reward Function
The reward function assumes the objective of the game is to move as far right as possible (increase the agent's x value), as fast as possible, without dying. To model this game, three separate variables compose the reward:

1. v: the difference in agent x values between states
- in this case this is instantaneous velocity for the given step
- v = x1 - x0
    - x0 is the x position before the step
    - x1 is the x position after the step
- moving right ⇔ v > 0
- moving left ⇔ v < 0
- not moving ⇔ v = 0

2. d: a death penalty that penalizes the agent for dying in a state
    - this penalty encourages the agent to avoid death
    - alive ⇔ d = 0
    - dead ⇔ d = -15
3. b : if the agent defeated the boss 
    - this reword will encourages the agent to defeat boss as possible
    - no defeated ⇔ 0
    - defeated ⇔ 30

So the reward function is:

<font color="#FF69B4">r = v + d + b</font>


> Note:The reward is clipped into the range (-15, 15).

## info dictionary
The info dictionary returned by the step method contains the following keys:

x_pos	int	Mario's x position in the stage (from the left)
y_pos	int	Mario's y position in the stage (from the bottom)

Key  | Type | Description |
---|--- | ---
life | int | The number of lives left, i.e., {3, 2, 1}
dead | Bool | Get The palyer is dead
done | Bool | Get the game is game over
status | Bool | Alive Status (00 - Dead, 01 - Alive, 02 - Dying)
x_pos | int | Player's x position in the stage (from the left)
y_pos |	int	| Player's y position in the stage (from the bottom)

