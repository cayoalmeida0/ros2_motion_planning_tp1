// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from amr_msgs:msg/Location.idl
// generated code does not contain a copyright notice

// IWYU pragma: private, include "amr_msgs/msg/location.h"


#ifndef AMR_MSGS__MSG__DETAIL__LOCATION__FUNCTIONS_H_
#define AMR_MSGS__MSG__DETAIL__LOCATION__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/action_type_support_struct.h"
#include "rosidl_runtime_c/message_type_support_struct.h"
#include "rosidl_runtime_c/service_type_support_struct.h"
#include "rosidl_runtime_c/type_description/type_description__struct.h"
#include "rosidl_runtime_c/type_description/type_source__struct.h"
#include "rosidl_runtime_c/type_hash.h"
#include "rosidl_runtime_c/visibility_control.h"
#include "amr_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "amr_msgs/msg/detail/location__struct.h"

/// Initialize msg/Location message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * amr_msgs__msg__Location
 * )) before or use
 * amr_msgs__msg__Location__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__Location__init(amr_msgs__msg__Location * msg);

/// Finalize msg/Location message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__Location__fini(amr_msgs__msg__Location * msg);

/// Create msg/Location message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * amr_msgs__msg__Location__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
amr_msgs__msg__Location *
amr_msgs__msg__Location__create(void);

/// Destroy msg/Location message.
/**
 * It calls
 * amr_msgs__msg__Location__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__Location__destroy(amr_msgs__msg__Location * msg);

/// Check for msg/Location message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__Location__are_equal(const amr_msgs__msg__Location * lhs, const amr_msgs__msg__Location * rhs);

/// Copy a msg/Location message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__Location__copy(
  const amr_msgs__msg__Location * input,
  amr_msgs__msg__Location * output);

/// Retrieve pointer to the hash of the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
const rosidl_type_hash_t *
amr_msgs__msg__Location__get_type_hash(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
const rosidl_runtime_c__type_description__TypeDescription *
amr_msgs__msg__Location__get_type_description(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the single raw source text that defined this type.
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
const rosidl_runtime_c__type_description__TypeSource *
amr_msgs__msg__Location__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support);

/// Retrieve pointer to the recursive raw sources that defined the description of this type.
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
const rosidl_runtime_c__type_description__TypeSource__Sequence *
amr_msgs__msg__Location__get_type_description_sources(
  const rosidl_message_type_support_t * type_support);

/// Initialize array of msg/Location messages.
/**
 * It allocates the memory for the number of elements and calls
 * amr_msgs__msg__Location__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__Location__Sequence__init(amr_msgs__msg__Location__Sequence * array, size_t size);

/// Finalize array of msg/Location messages.
/**
 * It calls
 * amr_msgs__msg__Location__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__Location__Sequence__fini(amr_msgs__msg__Location__Sequence * array);

/// Create array of msg/Location messages.
/**
 * It allocates the memory for the array and calls
 * amr_msgs__msg__Location__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
amr_msgs__msg__Location__Sequence *
amr_msgs__msg__Location__Sequence__create(size_t size);

/// Destroy array of msg/Location messages.
/**
 * It calls
 * amr_msgs__msg__Location__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__Location__Sequence__destroy(amr_msgs__msg__Location__Sequence * array);

/// Check for msg/Location message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__Location__Sequence__are_equal(const amr_msgs__msg__Location__Sequence * lhs, const amr_msgs__msg__Location__Sequence * rhs);

/// Copy an array of msg/Location messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__Location__Sequence__copy(
  const amr_msgs__msg__Location__Sequence * input,
  amr_msgs__msg__Location__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__MSG__DETAIL__LOCATION__FUNCTIONS_H_
