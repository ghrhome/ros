```angular2html
mkdir -p ~/my_workspace/src
cd ~/my_workspace/src
//ros的工作空间初始化命令
catkin_init_workspace
//
catkin_create_pkg my_package rospy
```

```angular2html
mkdir -p ~/my_workspace/src
cd ~/my_workspace/src
catkin_create_pkg my_package rospy
```


## 2. 为Python脚本添加执行权限：
```angular2html
chmod +x simple_publisher.py
```
## 构建ROS包：
```angular2html
cd ~/my_workspace
catkin_make
source devel/setup.bash



```
###运行ROS节点：
```angular2html
rosrun my_package simple_publisher.py
```

###这将启动名为simple_publisher的节点，该节点将发布消息到my_topic话题上。你可以使用rostopic echo命令来查看发布的消息：
```angular2html
rostopic echo my_topic
```
