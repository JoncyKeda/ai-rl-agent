import numpy as np

class SimpleEnv:
    def __init__(self):
        self.state_size = 10
        self.action_size = 2  # move left or right
        self.goal = 9

    def reset(self):
        self.state = 0
        return self.state

    def step(self, action):
        if action == 0:
            self.state = max(0, self.state - 1)
        else:
            self.state = min(self.goal, self.state + 1)

        reward = 1 if self.state == self.goal else -0.1
        done = self.state == self.goal

        return self.state, reward, done
