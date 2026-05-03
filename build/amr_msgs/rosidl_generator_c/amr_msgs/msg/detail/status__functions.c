// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from amr_msgs:msg/Status.idl
// generated code does not contain a copyright notice
#include "amr_msgs/msg/detail/status__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `extended_status`
// Member `status`
#include "rosidl_runtime_c/string_functions.h"
// Member `location`
#include "amr_msgs/msg/detail/location__functions.h"

bool
amr_msgs__msg__Status__init(amr_msgs__msg__Status * msg)
{
  if (!msg) {
    return false;
  }
  // extended_status
  if (!rosidl_runtime_c__String__init(&msg->extended_status)) {
    amr_msgs__msg__Status__fini(msg);
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    amr_msgs__msg__Status__fini(msg);
    return false;
  }
  // state_of_charge
  // localization_score
  // temperature
  // location
  if (!amr_msgs__msg__Location__init(&msg->location)) {
    amr_msgs__msg__Status__fini(msg);
    return false;
  }
  return true;
}

void
amr_msgs__msg__Status__fini(amr_msgs__msg__Status * msg)
{
  if (!msg) {
    return;
  }
  // extended_status
  rosidl_runtime_c__String__fini(&msg->extended_status);
  // status
  rosidl_runtime_c__String__fini(&msg->status);
  // state_of_charge
  // localization_score
  // temperature
  // location
  amr_msgs__msg__Location__fini(&msg->location);
}

bool
amr_msgs__msg__Status__are_equal(const amr_msgs__msg__Status * lhs, const amr_msgs__msg__Status * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // extended_status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->extended_status), &(rhs->extended_status)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  // state_of_charge
  if (lhs->state_of_charge != rhs->state_of_charge) {
    return false;
  }
  // localization_score
  if (lhs->localization_score != rhs->localization_score) {
    return false;
  }
  // temperature
  if (lhs->temperature != rhs->temperature) {
    return false;
  }
  // location
  if (!amr_msgs__msg__Location__are_equal(
      &(lhs->location), &(rhs->location)))
  {
    return false;
  }
  return true;
}

bool
amr_msgs__msg__Status__copy(
  const amr_msgs__msg__Status * input,
  amr_msgs__msg__Status * output)
{
  if (!input || !output) {
    return false;
  }
  // extended_status
  if (!rosidl_runtime_c__String__copy(
      &(input->extended_status), &(output->extended_status)))
  {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  // state_of_charge
  output->state_of_charge = input->state_of_charge;
  // localization_score
  output->localization_score = input->localization_score;
  // temperature
  output->temperature = input->temperature;
  // location
  if (!amr_msgs__msg__Location__copy(
      &(input->location), &(output->location)))
  {
    return false;
  }
  return true;
}

amr_msgs__msg__Status *
amr_msgs__msg__Status__create(void)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__Status * msg = (amr_msgs__msg__Status *)allocator.allocate(sizeof(amr_msgs__msg__Status), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(amr_msgs__msg__Status));
  bool success = amr_msgs__msg__Status__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
amr_msgs__msg__Status__destroy(amr_msgs__msg__Status * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    amr_msgs__msg__Status__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
amr_msgs__msg__Status__Sequence__init(amr_msgs__msg__Status__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__Status * data = NULL;

  if (size) {
    data = (amr_msgs__msg__Status *)allocator.zero_allocate(size, sizeof(amr_msgs__msg__Status), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = amr_msgs__msg__Status__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        amr_msgs__msg__Status__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
amr_msgs__msg__Status__Sequence__fini(amr_msgs__msg__Status__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      amr_msgs__msg__Status__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

amr_msgs__msg__Status__Sequence *
amr_msgs__msg__Status__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__Status__Sequence * array = (amr_msgs__msg__Status__Sequence *)allocator.allocate(sizeof(amr_msgs__msg__Status__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = amr_msgs__msg__Status__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
amr_msgs__msg__Status__Sequence__destroy(amr_msgs__msg__Status__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    amr_msgs__msg__Status__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
amr_msgs__msg__Status__Sequence__are_equal(const amr_msgs__msg__Status__Sequence * lhs, const amr_msgs__msg__Status__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!amr_msgs__msg__Status__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
amr_msgs__msg__Status__Sequence__copy(
  const amr_msgs__msg__Status__Sequence * input,
  amr_msgs__msg__Status__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(amr_msgs__msg__Status);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    amr_msgs__msg__Status * data =
      (amr_msgs__msg__Status *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!amr_msgs__msg__Status__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          amr_msgs__msg__Status__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!amr_msgs__msg__Status__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
