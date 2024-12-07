import gymnasium as gym
import random
from gymnasium.envs.toy_text.frozen_lake import *
import ui

#declare global variables
directions = ['left', 'down', 'right', 'up']

if __name__ == '__main__':
    # env = gym.make('FrozenLake-v1', desc=generate_random_map(size=4))
    # print(env.__getstate__())
    #create a random map with values from directions
    random_policy = []
    for i in range(4):
        random_policy.append([random.choice(directions) for j in range(4)])
    print(random_policy)
    print(ui.draw_policy(random_policy))
    #create a random map with values from 0 to 1
    val_map = generate_random_map(size=4)
    print(ui.draw_value(val_map))




