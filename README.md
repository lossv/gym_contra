# gym_contra
A gym game for Contra that for reinforcement learning for Python3.6 or Later

start random play with Src/ttt.py 

![image](https://github.com/OuYanghaoyue/gym_contra/blob/master/Img/TIM%E5%9B%BE%E7%89%8720190723143124.png)


Install enviroment on Ubuntu
```
pip3 install gym
pip3 install nes-py
```

Random play
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
