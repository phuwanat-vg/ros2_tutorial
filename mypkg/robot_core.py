import rclpy
from rclpy.node import Node

from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

class Robot(Node):
	def __init__(self):
		super().__init__('robot_core_node')
		self.wheel_radius = 0.06096 #m
		self.wheelbase = 0.225 #m
		
		self.max_rpm = 60.0 #rpm
		
		self.vel_sub = self.create_subscription(Twist, 'cmd_vel', self.vel_callback,10)
		
		self.leftwheel_pub = self.create_publisher(Float32, 'wheel_command_left', 10)
		self.rightwheel_pub = self.create_publisher(Float32, 'wheel_command_right', 10)
		
		self.v = 0.0
		self.w = 0.0
		
		self.timer = self.create_timer(0.1,self.timer_callback)
		
		self.cmd_l = Float32()
		self.cmd_r = Float32()
		self.get_logger().info("robot core is running")
		
		
		
		
		
	def vel_callback(self, vel):
		print("callback function")
		self.v = vel.linear.x
		self.w = vel.angular.z
		
		L = self.wheelbase
		R = self.wheel_radius
		
		v_r = ((2.0*self.v)+(self.w*L))/(2.0*R)
		v_l = ((2.0*self.v)-(self.w*L))/(2.0*R)
		
		self.wheel_speed_setpoint(v_r,v_l)
	def timer_callback(self):
		self.leftwheel_pub.publish(self.cmd_l)
		self.rightwheel_pub.publish(self.cmd_r)
	
	def wheel_speed_setpoint(self,vr,vl):
		rpm_r = vr*9.549297
		rpm_l = vl*9.549297  #1 rad/s = 9.549297 rpm
		
		rpm_r = max(min(rpm_r,self.max_rpm), -self.max_rpm)
		rpm_l = max(min(rpm_l,self.max_rpm), -self.max_rpm)
		
		if rpm_r == 0.0:
			self.cmd_r.data = 0.0
		if rpm_l == 0.0:
		 	self.cmd_l.data = 0.0
		self.cmd_r.data = rpm_r
		self.cmd_l.data = rpm_l	
		
		self.get_logger().info('out left rpm: %s' %rpm_l)
		self.get_logger().info('out right rpm: %s' %rpm_r)
		
def main():
	rclpy.init()
	
	rb = Robot()
	rclpy.spin(rb)
	
	rclpy.shutdown()
	
if __name__ == "__main__":
	main()
