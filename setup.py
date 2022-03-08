from setuptools import setup

import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share',package_name), glob("launch/*.launch.py")),
        (os.path.join('share',package_name,'config'), glob("config/*.yaml")),
        
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vm20',
    maintainer_email='phuwanat.aerod@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	"first_publisher = mypkg.first_node:main",
        	"twist_publisher = mypkg.twist_pub:main",
        	"first_subscription = mypkg.first_sub:main",
        	"twist_subscription = mypkg.twist_sub:main", 
        	"turtle_avoidance = mypkg.turtle_control:main", 
        	"first_param = mypkg.first_param:main",
        	"turtle_service_server = mypkg.turtle_service_server:main", 
        	"turtle_service_client = mypkg.turtle_service_client:main",
        	"pid_tuner = mypkg.pid_tuner:main",
        	"robot_core = mypkg.robot_core:main", 
        	
        ],
    },
)
