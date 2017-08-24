// Generated by gencpp from file snakebot_pushpoints/Pushpoints.msg
// DO NOT EDIT!


#ifndef SNAKEBOT_PUSHPOINTS_MESSAGE_PUSHPOINTS_H
#define SNAKEBOT_PUSHPOINTS_MESSAGE_PUSHPOINTS_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <std_msgs/Header.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Vector3.h>
#include <geometry_msgs/Point.h>

namespace snakebot_pushpoints
{
template <class ContainerAllocator>
struct Pushpoints_
{
  typedef Pushpoints_<ContainerAllocator> Type;

  Pushpoints_()
    : header()
    , centerContactLink(0)
    , contact_normals()
    , contact_tangents()
    , contact_positions()
    , link_numbers()
    , contact_sides()  {
    }
  Pushpoints_(const ContainerAllocator& _alloc)
    : header(_alloc)
    , centerContactLink(0)
    , contact_normals(_alloc)
    , contact_tangents(_alloc)
    , contact_positions(_alloc)
    , link_numbers(_alloc)
    , contact_sides(_alloc)  {
  (void)_alloc;
    }



   typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
  _header_type header;

   typedef int32_t _centerContactLink_type;
  _centerContactLink_type centerContactLink;

   typedef std::vector< ::geometry_msgs::Vector3_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::Vector3_<ContainerAllocator> >::other >  _contact_normals_type;
  _contact_normals_type contact_normals;

   typedef std::vector< ::geometry_msgs::Vector3_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::Vector3_<ContainerAllocator> >::other >  _contact_tangents_type;
  _contact_tangents_type contact_tangents;

   typedef std::vector< ::geometry_msgs::Point_<ContainerAllocator> , typename ContainerAllocator::template rebind< ::geometry_msgs::Point_<ContainerAllocator> >::other >  _contact_positions_type;
  _contact_positions_type contact_positions;

   typedef std::vector<int32_t, typename ContainerAllocator::template rebind<int32_t>::other >  _link_numbers_type;
  _link_numbers_type link_numbers;

   typedef std::vector<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > , typename ContainerAllocator::template rebind<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::other >  _contact_sides_type;
  _contact_sides_type contact_sides;




  typedef boost::shared_ptr< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> const> ConstPtr;

}; // struct Pushpoints_

typedef ::snakebot_pushpoints::Pushpoints_<std::allocator<void> > Pushpoints;

typedef boost::shared_ptr< ::snakebot_pushpoints::Pushpoints > PushpointsPtr;
typedef boost::shared_ptr< ::snakebot_pushpoints::Pushpoints const> PushpointsConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace snakebot_pushpoints

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': True}
// {'snakebot_pushpoints': ['/home/snake/Documents/catkin_ws/src/snakebot_pushpoints/msg'], 'geometry_msgs': ['/opt/ros/indigo/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/indigo/share/std_msgs/cmake/../msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> const>
  : TrueType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1259e13c987ab72fab3e94a351096f0b";
  }

  static const char* value(const ::snakebot_pushpoints::Pushpoints_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1259e13c987ab72fULL;
  static const uint64_t static_value2 = 0xab3e94a351096f0bULL;
};

template<class ContainerAllocator>
struct DataType< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "snakebot_pushpoints/Pushpoints";
  }

  static const char* value(const ::snakebot_pushpoints::Pushpoints_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Header header\n\
\n\
#middle contact link number\n\
int32 centerContactLink\n\
\n\
#normals\n\
geometry_msgs/Vector3[] contact_normals\n\
\n\
#forces\n\
geometry_msgs/Vector3[] contact_tangents\n\
\n\
#positions\n\
geometry_msgs/Point[] contact_positions\n\
\n\
#links in contact\n\
int32[] link_numbers\n\
\n\
#side of contact\n\
string[] contact_sides\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')\n\
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
================================================================================\n\
MSG: geometry_msgs/Vector3\n\
# This represents a vector in free space. \n\
# It is only meant to represent a direction. Therefore, it does not\n\
# make sense to apply a translation to it (e.g., when applying a \n\
# generic rigid transformation to a Vector3, tf2 will only apply the\n\
# rotation). If you want your data to be translatable too, use the\n\
# geometry_msgs/Point message instead.\n\
\n\
float64 x\n\
float64 y\n\
float64 z\n\
================================================================================\n\
MSG: geometry_msgs/Point\n\
# This contains the position of a point in free space\n\
float64 x\n\
float64 y\n\
float64 z\n\
";
  }

  static const char* value(const ::snakebot_pushpoints::Pushpoints_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.header);
      stream.next(m.centerContactLink);
      stream.next(m.contact_normals);
      stream.next(m.contact_tangents);
      stream.next(m.contact_positions);
      stream.next(m.link_numbers);
      stream.next(m.contact_sides);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Pushpoints_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::snakebot_pushpoints::Pushpoints_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::snakebot_pushpoints::Pushpoints_<ContainerAllocator>& v)
  {
    s << indent << "header: ";
    s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "centerContactLink: ";
    Printer<int32_t>::stream(s, indent + "  ", v.centerContactLink);
    s << indent << "contact_normals[]" << std::endl;
    for (size_t i = 0; i < v.contact_normals.size(); ++i)
    {
      s << indent << "  contact_normals[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "    ", v.contact_normals[i]);
    }
    s << indent << "contact_tangents[]" << std::endl;
    for (size_t i = 0; i < v.contact_tangents.size(); ++i)
    {
      s << indent << "  contact_tangents[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Vector3_<ContainerAllocator> >::stream(s, indent + "    ", v.contact_tangents[i]);
    }
    s << indent << "contact_positions[]" << std::endl;
    for (size_t i = 0; i < v.contact_positions.size(); ++i)
    {
      s << indent << "  contact_positions[" << i << "]: ";
      s << std::endl;
      s << indent;
      Printer< ::geometry_msgs::Point_<ContainerAllocator> >::stream(s, indent + "    ", v.contact_positions[i]);
    }
    s << indent << "link_numbers[]" << std::endl;
    for (size_t i = 0; i < v.link_numbers.size(); ++i)
    {
      s << indent << "  link_numbers[" << i << "]: ";
      Printer<int32_t>::stream(s, indent + "  ", v.link_numbers[i]);
    }
    s << indent << "contact_sides[]" << std::endl;
    for (size_t i = 0; i < v.contact_sides.size(); ++i)
    {
      s << indent << "  contact_sides[" << i << "]: ";
      Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.contact_sides[i]);
    }
  }
};

} // namespace message_operations
} // namespace ros

#endif // SNAKEBOT_PUSHPOINTS_MESSAGE_PUSHPOINTS_H
