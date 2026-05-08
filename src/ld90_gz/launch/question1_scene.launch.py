import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node


def generate_launch_description():
    pkg_ld90_gz = get_package_share_directory('ld90_gz')
    pkg_amr_description = get_package_share_directory('amr_description')
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    resource_paths = [
        pkg_ld90_gz,
        os.path.join(pkg_ld90_gz, 'obstacles'),
        os.path.join(pkg_ld90_gz, 'models'),
        os.path.dirname(pkg_amr_description)
    ]

    gz_resource_path_val = ':'.join(resource_paths)

    set_gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=gz_resource_path_val
    )

    world = os.path.join(pkg_ld90_gz, 'worlds', 'q1.sdf')
    model_file = os.path.join(pkg_ld90_gz, 'models', 'ld90_gz.sdf')
    bridge_file = os.path.join(pkg_ld90_gz, 'config', 'bridge.yaml')

    use_sim_time = LaunchConfiguration('use_sim_time')

    spawn_x = LaunchConfiguration('spawn_x')
    spawn_y = LaunchConfiguration('spawn_y')
    spawn_z = LaunchConfiguration('spawn_z')
    spawn_yaw = LaunchConfiguration('spawn_yaw')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={
            'gz_args': f'-r {world}'
        }.items()
    )

    spawn = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'ld90',
            '-file', model_file,
            '-x', spawn_x,
            '-y', spawn_y,
            '-z', spawn_z,
            '-Y', spawn_yaw
        ],
        output='screen'
    )

    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        parameters=[
            {'config_file': bridge_file},
            {'use_sim_time': use_sim_time}
        ],
        output='screen'
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true'
        ),

        DeclareLaunchArgument(
            'spawn_x',
            default_value='0.0',
            description='Initial x position of the LD90 robot.'
        ),

        DeclareLaunchArgument(
            'spawn_y',
            default_value='0.0',
            description='Initial y position of the LD90 robot.'
        ),

        DeclareLaunchArgument(
            'spawn_z',
            default_value='0.0',
            description='Initial z position of the LD90 robot.'
        ),

        DeclareLaunchArgument(
            'spawn_yaw',
            default_value='0.0',
            description='Initial yaw orientation of the LD90 robot in radians.'
        ),

        set_gz_resource_path,
        gz_sim,
        spawn,
        bridge
    ])