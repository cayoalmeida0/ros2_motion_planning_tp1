from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
import math

def generate_launch_description():
    controller = Node(
    package='ld90_gz',
    executable='tangent_bug',
    parameters=[
        {'goal_x': 10.0},
        {'goal_y': 0.0}
    ],
    output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'
        ),
        controller
    ])