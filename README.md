# ROS2-Action
This ROS2 package demonstrates simple and custom action implementations. It includes an example of creating and executing action servers and clients, showing how to define custom .action files and handle goal, feedback, and result communication for advanced robot task execution and control.
This ROS2 project demonstrates the creation and usage of custom actions. It consists of two packages — one defines a custom `.action` file, and the other implements an action server and client using that action. This example helps in understanding goal handling, feedback, and result management in ROS2.

---

## Overview

- **Create Action Package:** Defines a custom `.action` file (`Fibonacci.action`) specifying goal, feedback, and result messages.  
- **Simple Action Package:** Implements the action server and client using the custom action created in the first package.  
- The client sends a number as input, and the server continuously publishes feedback as it generates the Fibonacci sequence until completion.

---

## Features

- Create and build custom `.action` definitions in ROS2.  
- Implement a Fibonacci action server and client demonstrating goal–feedback–result flow.  
- Learn asynchronous communication between nodes using actions.  
- Observe real-time feedback as the Fibonacci series is generated.  
- Understand how actions differ from services for long-running tasks.

---

## Build Instructions

### Source ROS2 Environment
```bash
source /opt/ros/humble/setup.bash
```

### Clone Repository
```bash
git clone https://github.com/yashbhaskar/ROS2-Action.git
```

### Change Directory
```bash
cd ros_ws
```

### Build the Package
```bash
colcon build --packages-select simple_action_pkg create_action
source install/setup.bash
```

### Launch Action Server
```bash
ros2 run simple_action_pkg fibonacci_action_server
```

### Call Action Client
```bash
ros2 run simple_action_pkg fibonacci_action_client 5
```

### OR Call Action
```bash
ros2 action send_goal /fibonacci create_action/action/Fibonacci "{order: 5}"
```

---

## ✉️ Contact

📧 Yash Bhaskar – ybbhaskar19@gmail.com

📌 GitHub: https://github.com/yashbhaskar

