cmake_minimum_required(VERSION 2.8.3)
project(snakebot_position_control)

add_definitions(-std=c++11)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
	std_msgs
	geometry_msgs
	message_generation
)


add_message_files(
  FILES
  PositionControlEffort.msg
)

 generate_messages(
   DEPENDENCIES
   std_msgs
 )


catkin_package(
  CATKIN_DEPENDS message_runtime roscpp rospy std_msgs
)


include_directories(
  ${catkin_INCLUDE_DIRS}
)


add_executable(position_control 
	src/main.cpp
)
add_library(position_controller_class
	src/positioncontroller.cpp
)
add_library(vector_operators
	src/vectoroperators.cpp
)

add_dependencies(position_controller_class ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

add_dependencies(position_control ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})

target_link_libraries(position_control
	position_controller_class
	vector_operators
	${catkin_LIBRARIES}
)

