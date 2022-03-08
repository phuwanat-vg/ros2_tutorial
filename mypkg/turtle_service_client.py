import rclpy
from rclpy.node import Node

from std_srvs.srv import SetBool

import sys

class turtleClient(Node):
	def __init__(self):
		super().__init__("turtle_service_client_node")
		self.client = self.create_client(SetBool, 'start_stop_service')
		
		while not self.client.wait_for_service(timeout_sec = 1.0):
			print("...waiting for service...")
			
		self.request = SetBool.Request()
		
	def request_to_server(self):
		inp = sys.argv[1]
		
		if (inp == 'true') or (inp=='1'):
			self.request.data = True
		elif (inp=='false') or (inp=='0'):
			self.request.data = False
			
		self.future = self.client.call_async(self.request)
		
def main():
	rclpy.init()
	
	tc = turtleClient()
	tc.request_to_server()
	
	while rclpy.ok():
		rclpy.spin_once(tc)
		if tc.future.done():
			try:
				response = tc.future.result()
			except Exception as e:
				print(e)
			else:
				print('response: ', response.message)
			break

	rclpy.shutdown

if __name__=="__main__":
	main()
	
	
	
	
	
	
