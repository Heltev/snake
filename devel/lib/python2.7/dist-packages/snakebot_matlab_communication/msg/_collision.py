# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from snakebot_matlab_communication/collision.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import geometry_msgs.msg
import std_msgs.msg

class collision(genpy.Message):
  _md5sum = "e501bfb903e4dfcb8c45d45d37b998c0"
  _type = "snakebot_matlab_communication/collision"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

#link number
int32 link

#contact side (left or right)
string[] contact_sides

#normals
geometry_msgs/Vector3[] contact_normals

#tangents
geometry_msgs/Vector3[] contact_tangents

#positions
geometry_msgs/Point[] contact_positions
================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: geometry_msgs/Vector3
# This represents a vector in free space. 
# It is only meant to represent a direction. Therefore, it does not
# make sense to apply a translation to it (e.g., when applying a 
# generic rigid transformation to a Vector3, tf2 will only apply the
# rotation). If you want your data to be translatable too, use the
# geometry_msgs/Point message instead.

float64 x
float64 y
float64 z
================================================================================
MSG: geometry_msgs/Point
# This contains the position of a point in free space
float64 x
float64 y
float64 z
"""
  __slots__ = ['header','link','contact_sides','contact_normals','contact_tangents','contact_positions']
  _slot_types = ['std_msgs/Header','int32','string[]','geometry_msgs/Vector3[]','geometry_msgs/Vector3[]','geometry_msgs/Point[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,link,contact_sides,contact_normals,contact_tangents,contact_positions

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(collision, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.link is None:
        self.link = 0
      if self.contact_sides is None:
        self.contact_sides = []
      if self.contact_normals is None:
        self.contact_normals = []
      if self.contact_tangents is None:
        self.contact_tangents = []
      if self.contact_positions is None:
        self.contact_positions = []
    else:
      self.header = std_msgs.msg.Header()
      self.link = 0
      self.contact_sides = []
      self.contact_normals = []
      self.contact_tangents = []
      self.contact_positions = []

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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.link))
      length = len(self.contact_sides)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_sides:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.contact_normals)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_normals:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.contact_tangents)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_tangents:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.contact_positions)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_positions:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.contact_normals is None:
        self.contact_normals = None
      if self.contact_tangents is None:
        self.contact_tangents = None
      if self.contact_positions is None:
        self.contact_positions = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (self.link,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_sides = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.contact_sides.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_normals = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.contact_normals.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_tangents = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.contact_tangents.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_positions = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.contact_positions.append(val1)
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
      _x = self
      buff.write(_struct_3I.pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      if python3:
        buff.write(struct.pack('<I%sB'%length, length, *_x))
      else:
        buff.write(struct.pack('<I%ss'%length, length, _x))
      buff.write(_struct_i.pack(self.link))
      length = len(self.contact_sides)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_sides:
        length = len(val1)
        if python3 or type(val1) == unicode:
          val1 = val1.encode('utf-8')
          length = len(val1)
        if python3:
          buff.write(struct.pack('<I%sB'%length, length, *val1))
        else:
          buff.write(struct.pack('<I%ss'%length, length, val1))
      length = len(self.contact_normals)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_normals:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.contact_tangents)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_tangents:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
      length = len(self.contact_positions)
      buff.write(_struct_I.pack(length))
      for val1 in self.contact_positions:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.z))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.contact_normals is None:
        self.contact_normals = None
      if self.contact_tangents is None:
        self.contact_tangents = None
      if self.contact_positions is None:
        self.contact_positions = None
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _struct_3I.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (self.link,) = _struct_i.unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_sides = []
      for i in range(0, length):
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        start = end
        end += length
        if python3:
          val1 = str[start:end].decode('utf-8')
        else:
          val1 = str[start:end]
        self.contact_sides.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_normals = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.contact_normals.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_tangents = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Vector3()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.contact_tangents.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.contact_positions = []
      for i in range(0, length):
        val1 = geometry_msgs.msg.Point()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.z,) = _struct_3d.unpack(str[start:end])
        self.contact_positions.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_i = struct.Struct("<i")
_struct_3I = struct.Struct("<3I")
_struct_3d = struct.Struct("<3d")
