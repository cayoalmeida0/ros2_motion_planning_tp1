from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node

def generate_launch_description():
    controller = Node(
        package='ld90_gz',
        executable='potential_fields',
        output='screen',
        parameters=[
            {'goal_x': 6.0},
            {'goal_y': 0.0},
            {'attractive_gain': 1.0},
            {'repulsive_gain': 1.0},
            {'repulsive_threshold': 2.0},
            {'feedback_linearization_l': 0.3},
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