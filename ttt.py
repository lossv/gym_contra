from nes_py.wrappers import JoypadSpace
import gym
from Contra.actions import SIMPLE_MOVEMENT, COMPLEX_MOVEMENT, RIGHT_ONLY

env = gym.make('Contra-v0')
env = JoypadSpace(env, RIGHT_ONLY)

print("actions", env.action_space)
print("observation_space ", env.observation_space.shape[0])

done = False
a = env.reset()
print("a ", a)
for step in range(5000):
    if done:
        print("Over")
        break
    state, reward, done, info = env.step(env.action_space.sample())
    # print("state ", state)
    # print("reward ", reward)
    # print("Done ", done)
    print("score ", info['score'])
    env.render()

env.close()