#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    # 订阅到消息时的回调函数
    rospy.loginfo("Received message: %s", data.data)

def subscriber():
    # 初始化ROS节点
    rospy.init_node('simple_subscriber', anonymous=True)

    # 创建一个订阅者，订阅String类型的消息从'my_topic'话题
    rospy.Subscriber('my_topic', String, callback)

    # 进入循环以等待消息
    rospy.spin()

if __name__ == '__main__':
    subscriber()
