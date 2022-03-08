import rclpy

from rclpy.parameter import Parameter

from rclpy.node import Node

class testParam(Node):
	def __init__(self):
		super().__init__("parameter_test_node")
		
		self.declare_parameter('wheel_radius',10)
		self.declare_parameter('character','uni')
		
		self.timer = self.create_timer(0.5, self.timer_callback)
		
	def timer_callback(self):
		
		input_wheel_radius = self.get_parameter('wheel_radius')
		robot_type = self.get_parameter('character')
		
		print("wheel radius: ", input_wheel_radius.value)
		print("robot_type: ", robot_type.value)
		
def main():
	rclpy.init()
	tp = testParam()
	rclpy.spin(tp)
	
	rclpy.shutdown()
	
if __name__=="__main__":
	main()
	
	
	
	
