from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
	node1 = Node(
		package="mypkg",
		executable="first_publisher",
		remappings = [
			("number_topic","new_number_topic")
		])
		
	node2 = Node(
		package="mypkg",
		executable="first_subscription",
		remappings = [
			("number_topic","new_number_topic")
		])
	
	ld = LaunchDescription()
	
	ld.add_action(node1)
	ld.add_action(node2)
	
	return ld
