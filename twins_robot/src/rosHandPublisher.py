#!/usr/bin/env python

import rospy
import sys
sys.path.insert(0,"/home/melodic/ros_workspace/devel/lib/python2.7/dist-packages")
from twins_robot.msg import RobotArmCommand  
print(RobotArmCommand)

def publish_robot_arm_command():
    rospy.init_node('robot_arm_publisher', anonymous=True)
    pub = rospy.Publisher('robot_arm_commands', RobotArmCommand, queue_size=10)
    rate = rospy.Rate(1)  

    while not rospy.is_shutdown():
      
        command_msg = RobotArmCommand()

  
        command_msg.servo1_id = 1
        command_msg.servo1_pos = 45.0
        command_msg.servo1_time = 1.0

        pub.publish(command_msg)
        rospy.loginfo('RobotArmCommand message published')

        rate.sleep()

if __name__ == '__main__':
    try:
        publish_robot_arm_command()
    except rospy.ROSInterruptException:
        pass
