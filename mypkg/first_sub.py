import rclpy

from rclpy.node import Node

from std_msgs.msg import Int64

from rclpy import qos

class numberSub(Node):
	def __init__(self):
		super().__init__("number_subscription_node")
		
		self.number_sub = self.create_subscription(Int64, "number_topic",self.number_callback
			,qos_profile=qos.qos_profile_sensor_data)
		
		self.number_sub
		
	def number_callback(self,msg_in):
		new_msg = msg_in.data*2
		
		print("recieved message: ", msg_in.data)
		print("converted message: ",new_msg)
		
def main():
	rclpy.init()
	
	ns = numberSub()
	rclpy.spin(ns)
	
	rclpy.shutdown()
	
if __name__=="__main__":
	main()
	
