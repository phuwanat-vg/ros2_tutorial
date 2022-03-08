import rclpy
from rclpy.node import Node
from std_srvs.srv import SetBool

import sys

class exClient(Node):
	def __init__(self):
		super().__init__('start_client_node')
		self.client_ex = self.create_client(SetBool,'stp')
		
		while not self.client_ex.wait_for_service(timeout_sec=1.0):
			print("...waiting...")
		
		self.request = SetBool.Request()
		
	def request_to_server(self):
		inp = sys.argv[1]
		
		if (inp == 'on') or (inp=='1'):
			self.request.data = True
		elif (inp == 'off') or (inp=='0'):
			self.request.data = False
			
		self.future = self.client_ex.call_async(self.request)
		
def main():
	rclpy.init()
	ec = exClient()
	ec.request_to_server()
	while rclpy.ok():
		rclpy.spin_once(ec)
		if ec.future.done():
			try:
				response = ec.future.result()
			except Exception as e:
				print(e)
			
			else:
				ec.get_logger().info('response is %s :'%(response.message))
			break
	
	rclpy.shutdown()
	
if __name__=='__main__':
	main()
	
	
	
	
	
	





