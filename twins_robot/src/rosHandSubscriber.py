#!/usr/bin/env python

import rospy
import sys
sys.path.insert(0,"/home/melodic/ros_workspace/devel/lib/python2.7/dist-packages")
from twins_robot.msg import RobotArmCommand  

print(RobotArmCommand)

def robot_arm_callback(msg):
    rospy.loginfo('Received RobotArmCommand message:')
    rospy.loginfo('Servo 1: ID=%d, Pos=%.2f, Time=%.2f', msg.servo1_id, msg.servo1_pos, msg.servo1_time)


def subscribe_to_robot_arm_commands():
    rospy.init_node('robot_arm_subscriber', anonymous=True)
    rospy.Subscriber('robot_arm_commands', RobotArmCommand, robot_arm_callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        subscribe_to_robot_arm_commands()
    except rospy.ROSInterruptException:
        pass
