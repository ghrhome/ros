#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Int32  # Import String message
from timeit import default_timer as timer
import rosbag
import LeArm
import time

def publish_step(pub, step_data, bag):

    string_msg = String(data=step_data)  # Wrap the string in a String message
    pub.publish(string_msg)
    bag.write(pub.name, string_msg)
    rospy.sleep(1)

def main():
    rospy.init_node('record_commands')
    pub_robot_init = rospy.Publisher('init', String, queue_size=10)  # Use String message
    pub_set_servo = rospy.Publisher('setServo', String, queue_size=10)  # Use String message
    pub_recode_clone = rospy.Publisher('recode_clone', String, queue_size=10)  # Add a publisher for recode_clone
#    pub_sleep = rospy.Publisher('sleep',Int32, queue_size=10)  # Use String message
    bag = rosbag.Bag('recorded_steps.bag', 'w')

    def init_learm(init_data):
        init_data = [int(x) for x in init_data.split()]  # Convert space-separated string to list of integers
        LeArm.initLeArm(init_data)
        rospy.sleep(1)
    def set_servo(servo_msg):
        servo_data = [int(x) for x in servo_msg.split()]  # Convert space-separated string to list of integers
        servo_id, pos, time = servo_data[0], servo_data[1], servo_data[2]
        LeArm.setServo(servo_id, pos, time)
        rospy.sleep(1)
        
    try:
        sleep_data = 1  # Convert to string

        # Step 1: Initializing LeArm
        init_data = "0 0 0 0 0 0"  # Convert to string
        rospy.loginfo("Step 1: Initializing LeArm")
        publish_step(pub_robot_init, init_data, bag)
        init_learm(init_data)

        # Step 2: Setting servo 1 position to 1500
        servo_msg = "1 1000 1000"  # Convert to string
        set_servo(servo_msg)
        rospy.loginfo("Step 2: Setting servo 1 position to 1500")
        publish_step(pub_set_servo, servo_msg, bag)

        # Step 3: Setting servo sleep for 5 seconds
 #       sleep_msg = 5  # Convert to string
  #      rospy.loginfo("Step 3: Setting servo sleep for 5 seconds")
   #     publish_step(pub_sleep, sleep_msg, bag)

        # Step 4: Setting servo 2 position to 500
        servo_msg = "2 800 1500"  # Convert to string
        rospy.loginfo("Step 4: Setting servo 2 position to 500")
        set_servo(servo_msg)
        publish_step(pub_set_servo, servo_msg, bag)

        # Step 5: Setting servo sleep for 5 seconds
    #    sleep_msg = 5  # Convert to string
     #   rospy.loginfo("Step 5: Setting servo sleep for 5 seconds")
      #  publish_step(pub_sleep, sleep_msg, bag)
        pub_recode_clone.publish("start")
    except rospy.ROSInterruptException:
        pass

    finally:
        set_servo("1 1200 1200")
        set_servo("2 1200 1200")
        bag.close()

if __name__ == '__main__':
    main()

