from launch_ros.actions import Node
from launch import LaunchDescription

def generate_launch_description():
	node1 = Node(
		package="mypkg",
		executable="first_param",
		parameters = [
		{'wheel_radius': 25},
		{'character': "diff_drive"}
		],
		output='screen',
		emulate_tty=True
		)
		
	
	ld = LaunchDescription()
	
	ld.add_action(node1)
	
	
	return ld
