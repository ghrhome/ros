#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    # 初始化ROS节点
    rospy.init_node('simple_publisher', anonymous=True)

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
        publisher()
    except rospy.ROSInterruptException:
        pass
