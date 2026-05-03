// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:msg/Location.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "amr_msgs/msg/location.hpp"


#ifndef AMR_MSGS__MSG__DETAIL__LOCATION__TRAITS_HPP_
#define AMR_MSGS__MSG__DETAIL__LOCATION__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/msg/detail/location__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const Location & msg,
  std::ostream & out)
{
  out << "{";
  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: theta
  {
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const Location & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: theta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const Location & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::msg::Location & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::msg::Location & msg)
{
  return amr_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::msg::Location>()
{
  return "amr_msgs::msg::Location";
}

template<>
inline const char * name<amr_msgs::msg::Location>()
{
  return "amr_msgs/msg/Location";
}

template<>
struct has_fixed_size<amr_msgs::msg::Location>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::msg::Location>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::msg::Location>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__MSG__DETAIL__LOCATION__TRAITS_HPP_
