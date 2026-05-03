// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/Status.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "amr_msgs/msg/status.hpp"


#ifndef AMR_MSGS__MSG__DETAIL__STATUS__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_Status_location
{
public:
  explicit Init_Status_location(::amr_msgs::msg::Status & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::Status location(::amr_msgs::msg::Status::_location_type arg)
  {
    msg_.location = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::Status msg_;
};

class Init_Status_temperature
{
public:
  explicit Init_Status_temperature(::amr_msgs::msg::Status & msg)
  : msg_(msg)
  {}
  Init_Status_location temperature(::amr_msgs::msg::Status::_temperature_type arg)
  {
    msg_.temperature = std::move(arg);
    return Init_Status_location(msg_);
  }

private:
  ::amr_msgs::msg::Status msg_;
};

class Init_Status_localization_score
{
public:
  explicit Init_Status_localization_score(::amr_msgs::msg::Status & msg)
  : msg_(msg)
  {}
  Init_Status_temperature localization_score(::amr_msgs::msg::Status::_localization_score_type arg)
  {
    msg_.localization_score = std::move(arg);
    return Init_Status_temperature(msg_);
  }

private:
  ::amr_msgs::msg::Status msg_;
};

class Init_Status_state_of_charge
{
public:
  explicit Init_Status_state_of_charge(::amr_msgs::msg::Status & msg)
  : msg_(msg)
  {}
  Init_Status_localization_score state_of_charge(::amr_msgs::msg::Status::_state_of_charge_type arg)
  {
    msg_.state_of_charge = std::move(arg);
    return Init_Status_localization_score(msg_);
  }

private:
  ::amr_msgs::msg::Status msg_;
};

class Init_Status_status
{
public:
  explicit Init_Status_status(::amr_msgs::msg::Status & msg)
  : msg_(msg)
  {}
  Init_Status_state_of_charge status(::amr_msgs::msg::Status::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Status_state_of_charge(msg_);
  }

private:
  ::amr_msgs::msg::Status msg_;
};

class Init_Status_extended_status
{
public:
  Init_Status_extended_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Status_status extended_status(::amr_msgs::msg::Status::_extended_status_type arg)
  {
    msg_.extended_status = std::move(arg);
    return Init_Status_status(msg_);
  }

private:
  ::amr_msgs::msg::Status msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::Status>()
{
  return amr_msgs::msg::builder::Init_Status_extended_status();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__STATUS__BUILDER_HPP_
