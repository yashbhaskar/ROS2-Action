# ROS2-Action

This repository demonstrates a simple ROS 2 action implementation. It includes a basic action server and action client example to help understand asynchronous goal handling, feedback, and result communication in ROS 2. Ideal for beginners learning ROS 2 actions.

---

## 🤖 What is a ROS 2 Action?

### Definition
A **ROS 2 Action** is a communication mechanism used for **long-running tasks** that require:
- Continuous **feedback**
- The ability to **cancel** a task
- A final **result** when the task is completed

Actions are ideal when a task cannot be completed instantly and progress updates are required.

### Example Use Cases
- Robot navigation to a goal
- Pick-and-place operations
- Trajectory execution
- Long computations or processes

---

## 🧠 Why Use Actions Instead of Services?

| Feature        | Topic | Service | Action |
|---------------|-------|---------|--------|
| Continuous Data | ✅ | ❌ | ❌ |
| Request/Response | ❌ | ✅ | ❌ |
| Long Tasks | ❌ | ❌ | ✅ |
| Feedback | ❌ | ❌ | ✅ |
| Cancellation | ❌ | ❌ | ✅ |

---

## ⚙️ How ROS 2 Actions Work

A ROS 2 action consists of **three main components**:

1. **Goal**
   - Sent by the Action Client
   - Describes what task needs to be done

2. **Feedback**
   - Periodically sent by the Action Server
   - Provides progress updates while executing the goal

3. **Result**
   - Sent once the goal is completed, aborted, or canceled

### Action Communication Flow
1. Action Client sends a **goal** to the Action Server
2. Action Server accepts or rejects the goal
3. Action Server executes the task
4. Action Server publishes **feedback**
5. Action Server sends the **result**
6. Action Client receives the final status

---

## 📄 Action Definition File

An action file (`.action`) is divided into **three sections**:

```text
# Goal
int32 target

---
# Result
bool success

---
# Feedback
float32 progress
```
---

## ✨ Features of ROS 2 Actions

- ✅ Asynchronous execution  
- 🔁 Continuous feedback during execution  
- ⛔ Goal cancellation support  
- 🧵 Non-blocking communication  
- 🔌 Built on top of ROS 2 services and topics  
- 🛠 Suitable for complex robot behaviors  

---

## 🚀 Learning Outcomes

After using this repository, you will learn:

- ✔️ What ROS 2 actions are and when to use them  
- ✔️ Difference between Topics, Services, and Actions  
- ✔️ How to create a custom `.action` file  
- ✔️ How to implement an Action Server  
- ✔️ How to implement an Action Client  
- ✔️ How feedback, goals, and results work  
- ✔️ How to handle goal cancellation  
- ✔️ Best practices for long-running tasks in ROS 2  

---

## Installation

### Make Workspace
```bash
mkdir robot_ws/
```

### Change Workspace
```bash
cd robot_ws
```

### Make src
```bash
mkdir src/
```

### Change Workspace
```bash
cd src
```

### Clone This Repository
```bash
git clone https://github.com/yashbhaskar/ROS2-Action.git
```

### Change Workspace
```bash
cd ..
```

### Build the Package
```bash
colcon build --packages-select create_action simple_action_pkg
source install/setup.bash
```

---

## 🚀 How to Run

### Run Action Server

```bash
ros2 run simple_service_pkg service.py
```

### call action client

```bash
ros2 action send_goal /fibonacci create_action/action/Fibonacci "{order: 5}"
```

### OR 

```bash
ros2 run simple_action_pkg fibonacci_action_client
```

- The Action Server receives the goal (`order: 5`)
- Fibonacci sequence is calculated step-by-step
- Feedback is published during execution
- Final result returns the complete Fibonacci sequence

---

## ✉️ Contact

📧 Yash Bhaskar – ybbhaskar19@gmail.com

📌 GitHub: https://github.com/yashbhaskar
