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

    world = os.path.join(pkg_ld90_gz, 'worlds', 'q2.sdf')
    model_file = os.path.join(pkg_ld90_gz, 'models', 'ld90_gz.sdf')
    bridge_file = os.path.join(pkg_ld90_gz, 'config', 'bridge.yaml')
    use_sim_time = LaunchConfiguration('use_sim_time')

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments={'gz_args': f'-r {world}'}.items()
    )

    spawn = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=['-name', 'ld90', '-file', model_file, '-x', '0.0', '-y', '0.0', '-z', '0.0'],
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
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        set_gz_resource_path, # This now contains ALL the paths
        gz_sim,
        spawn,
        bridge
    ])