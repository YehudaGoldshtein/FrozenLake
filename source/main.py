import gymnasium as gym
env = gym.make('FrozenLake-v1')


if __name__ == '__main__':
    env.reset()
    env.render()
    env.step(1)
    env.render()
    env.step(1)
    env.render()
    env.step(2)
