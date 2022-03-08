#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64

from rclpy import qos

import random

class NumberNode(Node):
	
	def __init__(self):
		
		super().__init__("number_publisher_node")
		self.num_pub = self.create_publisher(Int64, "number_topic",
				qos_profile = qos.qos_profile_sensor_data)
		self.num_timer = self.create_timer(0.5, self.num_timer_callback)
		
	def num_timer_callback(self):
		random1 = random.randint(1,100)
		
		msg = Int64()
		msg.data = random1
		
		self.num_pub.publish(msg)
		
def main():
	rclpy.init()
	node = NumberNode()
	
	rclpy.spin(node)
	
	rclpy.shutdown()

if __name__=="__main__":
	main()

	
	
	
