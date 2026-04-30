import numpy as np

class QLearningAgent:
    def __init__(self, state_size, action_size):
        self.q_table = np.zeros((state_size, action_size))
        self.alpha = 0.1   # Learning rate
        self.gamma = 0.9   # Discount factor
        self.epsilon = 0.2 # Exploration rate

    def choose_action(self, state):
        if np.random.rand() < self.epsilon:
            return np.random.randint(len(self.q_table[state]))
        return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, next_state):
        predict = self.q_table[state][action]
        target = reward + self.gamma * np.max(self.q_table[next_state])

        self.q_table[state][action] += self.alpha * (target - predict)
