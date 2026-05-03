// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:msg/Location.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "amr_msgs/msg/location.h"


#ifndef AMR_MSGS__MSG__DETAIL__LOCATION__STRUCT_H_
#define AMR_MSGS__MSG__DETAIL__LOCATION__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>

// Constants defined in the message

/// Struct defined in msg/Location in the package amr_msgs.
/**
  * This contains the position of a point in free space
 */
typedef struct amr_msgs__msg__Location
{
  double x;
  double y;
  double theta;
} amr_msgs__msg__Location;

// Struct for a sequence of amr_msgs__msg__Location.
typedef struct amr_msgs__msg__Location__Sequence
{
  amr_msgs__msg__Location * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__msg__Location__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__MSG__DETAIL__LOCATION__STRUCT_H_
