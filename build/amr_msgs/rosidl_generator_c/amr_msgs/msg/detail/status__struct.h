// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:msg/Status.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "amr_msgs/msg/status.h"


#ifndef AMR_MSGS__MSG__DETAIL__STATUS__STRUCT_H_
#define AMR_MSGS__MSG__DETAIL__STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

// Include directives for member types
// Member 'extended_status'
// Member 'status'
#include "rosidl_runtime_c/string.h"
// Member 'location'
#include "amr_msgs/msg/detail/location__struct.h"

/// Struct defined in msg/Status in the package amr_msgs.
typedef struct amr_msgs__msg__Status
{
  rosidl_runtime_c__String extended_status;
  rosidl_runtime_c__String status;
  float state_of_charge;
  float localization_score;
  float temperature;
  amr_msgs__msg__Location location;
} amr_msgs__msg__Status;

// Struct for a sequence of amr_msgs__msg__Status.
typedef struct amr_msgs__msg__Status__Sequence
{
  amr_msgs__msg__Status * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__msg__Status__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__MSG__DETAIL__STATUS__STRUCT_H_
