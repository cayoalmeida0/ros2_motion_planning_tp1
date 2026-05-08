import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import math

def generate_launch_description():
    r1 = Node(
        package='ld90_gz',
        executable='potential_fields_follower',
        parameters=[
            {'scan_topic': '/r1/scan'},
            {'pose_topic': '/ld90_gt_1_pose'},
            {'neighbor_topics': ['/ld90_gt_2_pose']},
            {'curve_offset': 0.0},
            {'vel_topic':'/r1/cmd_vel'},
            {'controller_k': 1.0},
            {'feedback_linearization_l': 0.3},
            {'curve_size_multiplier': 5.0},
            {'curve_time_multiplier': 0.2},
            {'attractive_gain': 1.0},
            {'repulsive_gain': 1.0},
            {'repulsive_threshold': 2.0},
            {'max_speed': 1.0}
        ],
        output='screen'
    )
    r2 = Node(
        package='ld90_gz',
        executable='potential_fields_follower',
        parameters=[
            {'scan_topic': '/r2/scan'},
            {'pose_topic': 'ld90_gt_2_pose'},
            {'neighbor_topics': ['/ld90_gt_1_pose']},
            {'curve_offset': math.pi},
            {'vel_topic':'/r2/cmd_vel'},
            {'controller_k': 1.0},
            {'feedback_linearization_l': 0.3},
            {'curve_size_multiplier': 5.0},
            {'curve_time_multiplier': 0.2},
            {'attractive_gain': 1.0},
            {'repulsive_gain': 1.0},
            {'repulsive_threshold': 2.0},
            {'max_speed': 1.0}
        ],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'
        ),
        r1,r2
    ])