// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/Location.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "amr_msgs/msg/location.hpp"


#ifndef AMR_MSGS__MSG__DETAIL__LOCATION__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__LOCATION__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/location__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_Location_theta
{
public:
  explicit Init_Location_theta(::amr_msgs::msg::Location & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::Location theta(::amr_msgs::msg::Location::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::Location msg_;
};

class Init_Location_y
{
public:
  explicit Init_Location_y(::amr_msgs::msg::Location & msg)
  : msg_(msg)
  {}
  Init_Location_theta y(::amr_msgs::msg::Location::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_Location_theta(msg_);
  }

private:
  ::amr_msgs::msg::Location msg_;
};

class Init_Location_x
{
public:
  Init_Location_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Location_y x(::amr_msgs::msg::Location::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_Location_y(msg_);
  }

private:
  ::amr_msgs::msg::Location msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::Location>()
{
  return amr_msgs::msg::builder::Init_Location_x();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__LOCATION__BUILDER_HPP_
