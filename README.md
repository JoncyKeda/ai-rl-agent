# 🎮 AI Reinforcement Learning Agent (Q-Learning)

---

## 📌 Overview

This project implements a Reinforcement Learning (RL) agent using the Q-Learning algorithm. The agent learns to navigate an environment by interacting with it, receiving rewards, and improving its decisions over time.

Unlike traditional machine learning, this system does not rely on labeled data. Instead, it learns through **trial and error**, making it suitable for decision-making problems.

---

## 🎯 Objectives

* Understand Reinforcement Learning fundamentals
* Implement Q-Learning algorithm
* Train an agent to maximize rewards
* Visualize learning progress

---

## ✨ Features

* 🧠 Q-Learning algorithm implementation
* 🎮 Custom environment simulation
* 📊 Reward-based learning
* 📈 Training performance visualization
* ⚡ Lightweight and easy to run

---

## 🧠 Tech Stack

* **Python**
* **NumPy**
* **Matplotlib**

---

## 🏗️ System Architecture

```
Environment
   ↓
Agent takes Action
   ↓
Receives Reward
   ↓
Updates Q-Table
   ↓
Improves Policy
```

---

## 📂 Project Structure

```
ai-rl-agent/
│
├── main.py                # Training loop
├── requirements.txt
├── README.md
│
├── agent/
│   └── q_learning.py     # Q-learning logic
│
├── env/
│   └── environment.py    # Environment simulation
```

---

## ▶️ How to Run

### 1️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 2️⃣ Run the project

```
python main.py
```

---

## 💡 How It Works

### 🔹 Environment

* Agent starts at position 0
* Goal is to reach position 9

---

### 🔹 Actions

* Move left
* Move right

---

### 🔹 Rewards

* +1 → reaching goal
* -0.1 → each step

---

### 🔹 Learning

* Agent updates Q-values
* Learns best path over time

---

## 📊 Output

* Training progress graph
* Increasing rewards over episodes

---

## 🎯 Use Cases

* Game AI
* Robotics
* Autonomous systems
* Decision-making systems

---

## 👨‍💻 Author: 

"Joncy Keda - AI Developer"
---
