from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    controller = Node(
        package='ld90_gz',
        executable='curve_follower',
        output='screen',
        parameters=[
            {'controller_k': 1.0},
            {'feedback_linearization_l': 0.1},
            {'curve_size_multiplier': 3.0},
            {'curve_time_multiplier': 0.2},
            {'max_speed': 1.0}
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'
        ),
        controller
    ])