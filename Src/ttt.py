import gym
from Src import nesgym

# CartPole-v0
env = gym.make('Contra-v0')
# env = gym.make('CartPole-v0')
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

# import gym
# env = gym.make('Contra-v0')
# for i_episode in range(200):
#     env.render()
#     observation = env.reset()
#     for t in range(100):
#         # env.render()
#         # print(observation)
#         action = env.action_space.sample()
#         observation, reward, done, info = env.step(action)
#         if done:
#             print("Episode finished after {} timesteps".format(t+1))
#             break
# env.close()