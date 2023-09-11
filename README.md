# dexhand_description
ROS 2 URDF and Visualization for DexHand V1

![DexHand-DOF-Wave](https://github.com/iotdesignshop/dexhand_description/assets/2821763/5125b2f7-ebf4-45c6-b55d-e7e5ced13d0c)

## Overview
The DexHand is an open-source, dexterous humanoid robot hand that is designed to be manufactured using 3D printing and low-cost electronics. The project homepage can be found at http://www.dexhand.org.

This package provides:
- URDF for the DexHand robot hand
- RVIZ2 configuration for visualizing the hand with support for the ROS 2 Joint State Publisher GUI
- Launch files to make it easy to visualize the DexHand in RVIZ2

## Setup

### Assumptions
Use of this package assumes that you have a functional ROS 2 installation, and are familiar with the procedures for setting up workspaces, building packages, and running the ROS 2 command line tools. If not, there are [excellent tutorials available on the ROS 2 distribution pages](https://docs.ros.org/en/humble/Tutorials.html). We used [ROS 2 Humble Hawksbill](https://docs.ros.org/en/humble/index.html) for developing and testing this package, but it's generic enough that it should run fine with whatever version of ROS 2 you have installed.

### Setup Process
Setting up the package is like any other ROS 2 package you would build from source:

1) __Clone the GitHub Project__ into a ROS 2 workspace.

2) __Run rosdep__ to make sure you have all the dependencies.

3) __Run colcon__ to build the package

4) __Source the environment__ for the workspace

   
     
## Usage

Once you have the package built, you can use the included ROS 2 launchfile to start RVIZ2 and show the Joint State Publisher GUI:

`ros2 launch dexhand_description display.launch.py`

This should open the RVIZ2 window and display the hand along with the GUI which you can use to test the motion of all the joints

<img width="800" alt="Screenshot 2023-09-11 at 6 37 36 AM" src="https://github.com/iotdesignshop/dexhand_description/assets/2821763/f4967f8e-8c3e-4fc5-82f1-0c7c1afae3b3">

