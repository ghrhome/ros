为了实现两个节点之间的通信，你需要在两个不同的计算机上创建两个独立的ROS节点。以下是一个示例，演示如何分别在两台计算机上创建一个ROS节点。在这个示例中，一个节点将发布消息，另一个节点将订阅消息。

**在计算机1上创建发布者节点：**

1. 首先，在计算机1上创建一个ROS工作空间（如果尚未创建），并在其中创建一个包（package）。

```bash
mkdir -p ~/my_workspace/src
cd ~/my_workspace/src
catkin_create_pkg my_publisher rospy
```

2. 在`my_publisher`包的`src`文件夹中创建一个Python文件，例如`publisher_node.py`，并添加以下内容：

```python
#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher_node():
    # 初始化ROS节点
    rospy.init_node('publisher_node', anonymous=True)

    # 创建一个发布者，发布String类型的消息到'my_topic'话题
    pub = rospy.Publisher('my_topic', String, queue_size=10)

    # 设置发布频率
    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
        # 创建一个字符串消息
        message = "Hello, ROS!"

        # 发布消息
        pub.publish(message)

        # 打印消息
        rospy.loginfo(message)

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher_node()
    except rospy.ROSInterruptException:
        pass
```

3. 为Python脚本添加执行权限：

```bash
chmod +x publisher_node.py
```

4. 构建ROS包：

```bash
cd ~/my_workspace
catkin_make
source devel/setup.bash
```

5. 运行发布者节点：

```bash
rosrun my_publisher publisher_node.py
```

**在计算机2上创建订阅者节点：**

1. 在计算机2上创建一个ROS工作空间（如果尚未创建），并在其中创建一个包。

```bash
mkdir -p ~/my_workspace/src
cd ~/my_workspace/src
catkin_create_pkg my_subscriber rospy
```

2. 在`my_subscriber`包的`src`文件夹中创建一个Python文件，例如`subscriber_node.py`，并添加以下内容：

```python
#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    # 订阅到消息时的回调函数
    rospy.loginfo("Received message: %s", data.data)

def subscriber_node():
    # 初始化ROS节点
    rospy.init_node('subscriber_node', anonymous=True)

    # 创建一个订阅者，订阅String类型的消息从'my_topic'话题
    rospy.Subscriber('my_topic', String, callback)

    # 进入循环以等待消息
    rospy.spin()

if __name__ == '__main__':
    subscriber_node()
```

3. 为Python脚本添加执行权限：

```bash
chmod +x subscriber_node.py
```

4. 构建ROS包：

```bash
cd ~/my_workspace
catkin_make
source devel/setup.bash
```

5. 运行订阅者节点：

```bash
rosrun my_subscriber subscriber_node.py
```

现在，计算机1上的发布者节点将发布消息到`my_topic`话题，而计算机2上的订阅者节点将接收并显示这些消息。这样，你就建立了两个独立的ROS节点，它们可以在不同的计算机上进行通信。