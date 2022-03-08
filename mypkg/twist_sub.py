import rclpy

from rclpy.node import Node

from geometry_msgs.msg import Twist

from rclpy import qos

class twistSub(Node):
	def __init__(self):
		super().__init__("twist_subscriber_node")
		
		self.vel_sub = self.create_subscription(Twist, "cmd_vel",self.vel_callback
			,qos_profile=qos.qos_profile_system_default)
		
		self.vel_sub
		
	def vel_callback(self,msg_in):
		linear_x = msg_in.linear.x
		angular_z = msg_in.angular.z
		
		sum_vel = linear_x + angular_z
		
		print("sum_vel: ", sum_vel)
		
def main():
	rclpy.init()
	
	ns = twistSub()
	rclpy.spin(ns)
	
	rclpy.shutdown()
	
if __name__=="__main__":
	main()
	
