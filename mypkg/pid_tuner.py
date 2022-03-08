import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3

class Tuner(Node):

    def __init__(self):
        super().__init__('pid_tuner_node')
        self.setpoint_pub = self.create_publisher(Twist, 'wr_command', 10)
        self.pid_gain_pub = self.create_publisher(Vector3, 'pid_gain', 10)
        
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.declare_parameter('KP', 0.0)
        self.declare_parameter('KI', 0.0)
        self.declare_parameter('KD', 0.0)

    def timer_callback(self):
    	controller_gain = Vector3()
    	kp = self.get_parameter('KP').value
    	ki = self.get_parameter('KI').value
    	kd = self.get_parameter('KD').value
    	
    	controller_gain.x = kp
    	controller_gain.y = ki
    	controller_gain.z = kd
    	
    	self.pid_gain_pub.publish(controller_gain)
    	
    	print("controller gain: ",controller_gain)

def main(args=None):
    rclpy.init(args=args)

    tn = Tuner()

    rclpy.spin(tn)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    tn.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
