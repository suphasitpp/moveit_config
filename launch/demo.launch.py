from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import PathJoinSubstitution
from moveit_configs_utils import MoveItConfigsBuilder
from moveit_configs_utils.launches import generate_move_group_launch

def generate_launch_description():
    moveit_config = MoveItConfigsBuilder("med7attached", package_name="moveit_config").to_moveit_configs()

    # Path to custom RViz config
    rviz_config_file = PathJoinSubstitution([
        FindPackageShare("da_vinci_tool_integration"),
        "rviz",
        "my_robot_config.rviz"
    ])

    return LaunchDescription([
        # Robot State Publisher only (no joint_state_publisher)
        Node(
            package="robot_state_publisher",
            executable="robot_state_publisher",
            name="robot_state_publisher",
            parameters=[moveit_config.robot_description],
            output="screen"
        ),

        # Move Group Node (IK, planning)
        generate_move_group_launch(moveit_config),

        # RViz2 with custom config
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            arguments=["-d", rviz_config_file],
            parameters=[moveit_config.robot_description,
                       moveit_config.robot_description_semantic],
            output="screen"
        )
    ])
