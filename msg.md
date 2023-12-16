在ROS中，通常会在主机（Master）上启动`roscore`，而在从机上启动节点。`roscore`是ROS的主要控制节点，它协调所有ROS节点之间的通信。以下是一些关于在主机和从机上启动`roscore`和节点的指导原则：

1. **在主机上启动 `roscore`**：

   - 通常，`roscore`应该在主机上启动，因为它充当整个ROS系统的主要控制中心。在主机上运行`roscore`会创建ROS主节点，用于管理通信，参数服务器和其他ROS核心功能。
   
   - 在主机上打开终端，并运行以下命令启动`roscore`：

     ```bash
     roscore
     ```

   - 一旦`roscore`在主机上启动，你可以在任何连接到同一ROS网络的计算机上运行ROS节点。

2. **在从机上启动节点**：

   - 从机上的节点通常在主机上启动了`roscore`后才能启动。节点可以通过指定主机的IP地址或主机名来连接到主机上运行的`roscore`。

   - 在从机上，你可以使用以下命令来运行ROS节点，连接到主机上的`roscore`：

     ```bash
     export ROS_MASTER_URI=http://主机的IP地址:11311
     ```

     将`主机的IP地址`替换为运行`roscore`的主机的实际IP地址。

   - 然后，在从机上启动节点，例如：

     ```bash
     rosrun my_package my_node.py
     ```

     请确保`ROS_MASTER_URI`已正确设置，以便节点能够与主机上的`roscore`通信。

通过这种方式，你可以在主机上启动`roscore`，然后在从机上启动ROS节点，实现主从机模式下的ROS通信和控制。