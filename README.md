# gym_contra
A gym game for Contra that for reinforcement learning for Python3.6 or Later

start with Src/ttt.py 

Install enviroment on Ubuntu
```
pip3 install gym
pip3 install nes-py
```

Random play
```
import gym
from Src import nesgym

env = gym.make('Contra-v0')

obs = env.reset()

print("Make done")

print("action", env.action_space)
env.render()
print(env.observation_space)
for step in range(100000):
    env.render()
    action = env.action_space.sample()
    # print("action", env.action_space)
    obs, reward, done, info = env.step(action)
env.close()
```
