from nes_py.wrappers import JoypadSpace
from Src.Env.actions import SIMPLE_MOVEMENT, COMPLEX_MOVEMENT, RIGHT_ONLY
import gym

env = gym.make('Contra-v0')
env = JoypadSpace(env, RIGHT_ONLY)

done = False
env.reset()
for step in range(5000):
    if done:
        print("Over")
        break
    state, reward, done, info = env.step(env.action_space.sample())
    env.render()

env.close()