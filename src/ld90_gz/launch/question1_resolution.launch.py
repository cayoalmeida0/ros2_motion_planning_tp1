from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue


def generate_launch_description():

    goal_x = LaunchConfiguration('goal_x')
    goal_y = LaunchConfiguration('goal_y')
    use_sim_time = LaunchConfiguration('use_sim_time')

    controller = Node(
        package='ld90_gz',
        executable='tangent_bug',
        parameters=[
            {
                'use_sim_time': ParameterValue(use_sim_time, value_type=bool),
                'goal_x': ParameterValue(goal_x, value_type=float),
                'goal_y': ParameterValue(goal_y, value_type=float),
            }
        ],
        output='screen'
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation time'
        ),

        DeclareLaunchArgument(
            'goal_x',
            default_value='6.0',
            description='Goal position in x axis.'
        ),

        DeclareLaunchArgument(
            'goal_y',
            default_value='0.0',
            description='Goal position in y axis.'
        ),

        controller
    ])