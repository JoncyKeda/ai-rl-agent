from agent.q_learning import QLearningAgent
from env.environment import SimpleEnv
import matplotlib.pyplot as plt

episodes = 500

env = SimpleEnv()
agent = QLearningAgent(state_size=env.state_size, action_size=env.action_size)

rewards = []

for ep in range(episodes):
    state = env.reset()
    total_reward = 0

    done = False

    while not done:
        action = agent.choose_action(state)
        next_state, reward, done = env.step(action)

        agent.learn(state, action, reward, next_state)

        state = next_state
        total_reward += reward

    rewards.append(total_reward)

print("✅ Training Complete")

# Plot rewards
plt.plot(rewards)
plt.title("Training Progress")
plt.xlabel("Episodes")
plt.ylabel("Reward")
plt.show()
