#! /usr/bin/env python3

import rospy
import time
from std_msgs.msg import Float64

rospy.init_node('kasimx_control_init')
pub1 = rospy.Publisher('/kasimx/joint1_velocity_controller/command', Float64, queue_size=1)
count1 = Float64()

pub2 = rospy.Publisher('/kasimx/joint2_velocity_controller/command', Float64, queue_size=1)
count2 = Float64()

count1.data = -0.8
count2.data = 1.0
pub1.publish(count1)
pub2.publish(count2)
time.sleep(5)
count1.data = -0.8
count2.data = 1.0
pub1.publish(count1)
pub2.publish(count2)