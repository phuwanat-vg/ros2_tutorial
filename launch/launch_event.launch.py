from launch_ros.actions import Node
from launch import LaunchDescription

from launch.event_handlers import (OnExecutionComplete, OnProcessExit, OnProcessIO,
 				 OnProcessStart, OnShutdown)

from launch.actions import (RegisterEventHandler, LogInfo)

def generate_launch_description():
	node1 = Node(
		package="mypkg",
		executable="first_publisher")
		
	node2 = Node(
		package="mypkg",
		executable="first_subscription")

	
	return LaunchDescription([
		node1,
		RegisterEventHandler(
			OnProcessStart(
				target_action=node1,
				on_start=[
					LogInfo(msg='Node1 started'),
					node2,
				]
			)
		),
		RegisterEventHandler(
			OnProcessStart(
				target_action=node2,
				on_start=[
					LogInfo(msg='Now, Node2 started'),
				]
			)
		),
		RegisterEventHandler(
			OnShutdown(
				on_shutdown= [
					LogInfo(msg= 'Launch file was asked to shutdown'),
				]
			)
		)

	
	])
