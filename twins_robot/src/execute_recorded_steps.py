#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import rosbag
import LeArm

#init_data =null

def execute_recorded_steps(bag_filename):
    bag = rosbag.Bag(bag_filename, 'r')

    def init_learm(init_data):
        init_data = [int(x) for x in init_data.split()]
        LeArm.initLeArm(init_data)
#        rospy.sleep(1)
    
    def set_servo(servo_msg):
        servo_data = [int(x) for x in servo_msg.split()]
        servo_id, pos, time = servo_data[0], servo_data[1], servo_data[2]
        LeArm.setServo(servo_id, pos, time)

 #       rospy.sleep(1)

    init_data = None
    for topic, msg, t in bag.read_messages():
        rospy.loginfo("Received 'init' message: topic={}, data={}, timestamp={}".format(topic, msg, t))
        rospy.loginfo(init_data)

        if topic == 'init':

            init_data = msg.data
            init_learm(init_data)
        #    rospy.loginfo(init_data)
        if topic == 'setServo':
            set_servo(msg.data)
        elif topic == 'sleep':
            rospy.sleep(int(msg.data))

    bag.close()
    rospy.loginfo("done")
    rospy.signal_shutdown("Shutting down")
def recode_clone_callback(data):
    if data.data == "start":
        rospy.loginfo("Received 'start' message. Executing recorded steps...")
        execute_recorded_steps('recorded_steps.bag')
        #rospy.sleep(1)

if __name__ == '__main__':
    rospy.init_node('execute_recorded_steps')
    rospy.Subscriber('recode_clone', String, recode_clone_callback)
    rospy.spin()

