import rclpy

from std_srvs.srv import SetBool

from rclpy.node import Node

from rclpy import qos

from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class turtleControl(Node):
	def __init__(self):
		super().__init__("tuetle_avoidance")
		self.vel_pub = self.create_publisher(Twist, "turtle1/cmd_vel",10)
		self.pose_sub = self.create_subscription(Pose, "turtle1/pose", self.pose_callback, 
				qos_profile = qos.qos_profile_sensor_data)
				
		self.vel_timer = self.create_timer(0.05, self.vel_timer_callback)
		self.x = 0.0
		self.y = 0.0
		
		self.v = 0.0
		self.w = 0.0
		
		self.srv = self.create_service(SetBool,'stp', self.start_stop_callback)
		self.trigger = 0
		
	def start_stop_callback(self,request,response):
		self.get_logger().info("Request is: %s"%(request.data))
		
		if request.data:
			print("the turtle start moving")
			response.success = True
			response.message = "Yout turtle is moving"
			self.trigger = 1
		else:
			print("Try to stop")
			response.success = True
			response.message = "Yout turtle is stopped"
			self.trigger = 0
		return response
		
	def pose_callback(self,pose_in):
		self.x = pose_in.x
		self.y = pose_in.y
		
		print("x: {} y: {}".format(self.x,self.y))
		
		if (self.trigger == 1) :
			self.collision_check()
		else:
			self.stop()
	
	def stop(self):
		self.v = 0.0
		self.w = 0.0
	
	def collision_check(self):
		if (self.x>=8 or self.x<=2 or self.y<=2 or self.y>=8):
			self.v = 0.3
			self.w = 1.0
		else:
			self.v = 0.5
			self.w = 0.0
			
		
	def vel_timer_callback(self):
		cmd_vel = Twist()
		cmd_vel.linear.x = self.v
		cmd_vel.angular.z = self.w
		
		self.vel_pub.publish(cmd_vel)
		
def main():
	rclpy.init()
	tc = turtleControl()
	
	rclpy.spin(tc)
	
	rclpy.shutdown()
	
if __name__=="__main__":
	main()
	
	
