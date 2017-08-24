# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "snakebot_propulsion_control: 1 messages, 0 services")

set(MSG_I_FLAGS "-Isnakebot_propulsion_control:/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg;-Istd_msgs:/opt/ros/indigo/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(genlisp REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(snakebot_propulsion_control_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg" NAME_WE)
add_custom_target(_snakebot_propulsion_control_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "snakebot_propulsion_control" "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg" ""
)

#
#  langs = gencpp;genlisp;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(snakebot_propulsion_control
  "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snakebot_propulsion_control
)

### Generating Services

### Generating Module File
_generate_module_cpp(snakebot_propulsion_control
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snakebot_propulsion_control
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(snakebot_propulsion_control_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(snakebot_propulsion_control_generate_messages snakebot_propulsion_control_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg" NAME_WE)
add_dependencies(snakebot_propulsion_control_generate_messages_cpp _snakebot_propulsion_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snakebot_propulsion_control_gencpp)
add_dependencies(snakebot_propulsion_control_gencpp snakebot_propulsion_control_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snakebot_propulsion_control_generate_messages_cpp)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(snakebot_propulsion_control
  "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snakebot_propulsion_control
)

### Generating Services

### Generating Module File
_generate_module_lisp(snakebot_propulsion_control
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snakebot_propulsion_control
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(snakebot_propulsion_control_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(snakebot_propulsion_control_generate_messages snakebot_propulsion_control_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg" NAME_WE)
add_dependencies(snakebot_propulsion_control_generate_messages_lisp _snakebot_propulsion_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snakebot_propulsion_control_genlisp)
add_dependencies(snakebot_propulsion_control_genlisp snakebot_propulsion_control_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snakebot_propulsion_control_generate_messages_lisp)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(snakebot_propulsion_control
  "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snakebot_propulsion_control
)

### Generating Services

### Generating Module File
_generate_module_py(snakebot_propulsion_control
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snakebot_propulsion_control
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(snakebot_propulsion_control_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(snakebot_propulsion_control_generate_messages snakebot_propulsion_control_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/snake/Documents/catkin_ws/src/snakebot_propulsion_control/msg/PropulsionEffort.msg" NAME_WE)
add_dependencies(snakebot_propulsion_control_generate_messages_py _snakebot_propulsion_control_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(snakebot_propulsion_control_genpy)
add_dependencies(snakebot_propulsion_control_genpy snakebot_propulsion_control_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS snakebot_propulsion_control_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snakebot_propulsion_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/snakebot_propulsion_control
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(snakebot_propulsion_control_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snakebot_propulsion_control)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/snakebot_propulsion_control
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(snakebot_propulsion_control_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snakebot_propulsion_control)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snakebot_propulsion_control\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/snakebot_propulsion_control
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(snakebot_propulsion_control_generate_messages_py std_msgs_generate_messages_py)
endif()
