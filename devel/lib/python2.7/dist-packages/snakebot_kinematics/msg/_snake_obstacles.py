# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from snakebot_kinematics/snake_obstacles.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import snakebot_kinematics.msg

class snake_obstacles(genpy.Message):
  _md5sum = "b58eaeba4fdc2fe74e0b3582ba64166f"
  _type = "snakebot_kinematics/snake_obstacles"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """obstacles obstaclePose
kinematics snakePose

================================================================================
MSG: snakebot_kinematics/obstacles
int32[] number				  # obstacle numbers
geometry_msgs/Pose2D[] pose

================================================================================
MSG: geometry_msgs/Pose2D
# This expresses a position and orientation on a 2D manifold.

float64 x
float64 y
float64 theta
================================================================================
MSG: snakebot_kinematics/kinematics
int32[] number	# link numbers
geometry_msgs/Pose2D[] pose"""
  __slots__ = ['obstaclePose','snakePose']
  _slot_types = ['snakebot_kinematics/obstacles','snakebot_kinematics/kinematics']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       obstaclePose,snakePose

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(snake_obstacles, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.obstaclePose is None:
        self.obstaclePose = snakebot_kinematics.msg.obstacles()
      if self.snakePose is None:
        self.snakePose = snakebot_kinematics.msg.kinematics()
    else:
      self.obstaclePose = snakebot_kinematics.msg.obstacles()
      self.snakePose = snakebot_kinematics.msg.kinematics()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.obstaclePose.number)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.obstaclePose.number))
      length = len(self.obstaclePose.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstaclePose.pose:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.theta))
      length = len(self.snakePose.number)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(struct.pack(pattern, *self.snakePose.number))
      length = len(self.snakePose.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.snakePose.pose:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.theta))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.obstaclePose is None:
        self.obstaclePose = snakebot_kinematics.msg.obstacles()
      if self.snakePose is None:
        self.snakePose = snakebot_kinematics.msg.kinematics()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.obstaclePose.number = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstaclePose.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose2D()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _struct_3d.unpack(str[start:end])
        self.obstaclePose.pose.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.snakePose.number = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.snakePose.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose2D()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _struct_3d.unpack(str[start:end])
        self.snakePose.pose.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.obstaclePose.number)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.obstaclePose.number.tostring())
      length = len(self.obstaclePose.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.obstaclePose.pose:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.theta))
      length = len(self.snakePose.number)
      buff.write(_struct_I.pack(length))
      pattern = '<%si'%length
      buff.write(self.snakePose.number.tostring())
      length = len(self.snakePose.pose)
      buff.write(_struct_I.pack(length))
      for val1 in self.snakePose.pose:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.theta))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.obstaclePose is None:
        self.obstaclePose = snakebot_kinematics.msg.obstacles()
      if self.snakePose is None:
        self.snakePose = snakebot_kinematics.msg.kinematics()
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.obstaclePose.number = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.obstaclePose.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose2D()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _struct_3d.unpack(str[start:end])
        self.obstaclePose.pose.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%si'%length
      start = end
      end += struct.calcsize(pattern)
      self.snakePose.number = numpy.frombuffer(str[start:end], dtype=numpy.int32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.snakePose.pose = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Pose2D()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _struct_3d.unpack(str[start:end])
        self.snakePose.pose.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3d = struct.Struct("<3d")
