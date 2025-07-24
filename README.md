# MoveIt Configuration Package

This package contains MoveIt configuration files for robotic motion planning and control of the KUKA LBR Med7 arm with da Vinci PSM tool integration.

## Description

This is a MoveIt configuration package generated using the MoveIt Setup Assistant for robotic arm motion planning. It includes all necessary configuration files for:

- Motion planning parameters and algorithms
- Joint limits and kinematics configuration
- Planning scene and collision detection setup
- Launch files for MoveIt planning execution
- RViz visualization configuration

## Dependencies

- ROS 2 Humble
- MoveIt 2
- `da_vinci_tool_integration` package (robot description)
- Standard ROS 2 packages: `robot_state_publisher`, `joint_state_publisher_gui`, `rviz2`

## Usage

Launch the MoveIt planning execution with:

```bash
# Launch MoveIt demo (includes RViz)
ros2 launch moveit_config demo.launch.py

# Launch MoveIt move_group server only
ros2 launch moveit_config move_group.launch.py

# Launch RViz with MoveIt plugin
ros2 launch moveit_config moveit_rviz.launch.py
```

## Package Structure

- `config/` - Configuration files for MoveIt planning
  - `joint_limits.yaml` - Joint velocity and acceleration limits
  - `kinematics.yaml` - Kinematics solver configuration
  - `moveit_controllers.yaml` - Controller configuration
  - `*.srdf` - Semantic robot description
  - `*.urdf.xacro` - Robot description with MoveIt additions
- `launch/` - Launch files for starting MoveIt components
  - `demo.launch.py` - Complete MoveIt demo with RViz
  - `move_group.launch.py` - MoveIt planning server
  - `moveit_rviz.launch.py` - RViz with MoveIt plugin
- `.setup_assistant` - MoveIt Setup Assistant configuration

## Robot Configuration

This configuration is specifically designed for:
- **Robot:** KUKA LBR Med7 arm
- **End-effector:** da Vinci PSM tool with adaptor
- **Planning Group:** Complete arm chain for motion planning
- **Kinematics Solver:** Configured for 7-DOF arm kinematics

## Notes

- This package was generated using the MoveIt Setup Assistant
- Requires the `da_vinci_tool_integration` package for robot description
- Configured for simulation and real robot control
- Planning algorithms and parameters are optimized for surgical robotics applications

## License

MIT License (or your chosen license)

---

## Contact

For questions or contributions, open an issue or pull request on GitHub. 