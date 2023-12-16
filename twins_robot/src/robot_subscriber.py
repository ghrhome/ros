#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def publisher():
    rospy.init_node('simple_publisher', anonymous=True)

    pub = rospy.Publisher('my_topic', String, queue_size=10)

    rate = rospy.Rate(1)  # 1 Hz

    while not rospy.is_shutdown():
    
        message = "Hello, ROS!"

        pub.publish(message)

        rospy.loginfo(message)

        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass

