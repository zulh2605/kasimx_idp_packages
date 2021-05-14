#! /usr/bin/env python3

import rospy
import time
from std_msgs.msg import Float64

rospy.init_node('kasimx_control_publisher')
pub1 = rospy.Publisher('/kasimx/joint1_velocity_controller/command', Float64, queue_size=1)
count1 = Float64()

pub2 = rospy.Publisher('/kasimx/joint2_velocity_controller/command', Float64, queue_size=1)
count2 = Float64()


while not rospy.is_shutdown(): 
  cmd=input("Enter command string: ")
  if cmd=="init":
  	count1.data = -1.0
  	count2.data = 1.0
  elif cmd=="seq0":
    count1.data = 0.5
    count2.data = -1.5
  elif cmd=="seq1":
  	count1.data = 0.0
  	count2.data = -1.0
  elif cmd=="seq2":
  	count1.data = 1.0
  	count2.data = 0.0
  elif cmd=="seq3":
  	count1.data = -0.2
  	count2.data = 0.3
  elif cmd=="stop":
  	count1.data = 0.0
  	count2.data = 0.0
  pub1.publish(count1)
  pub2.publish(count2)
  time.sleep(1)