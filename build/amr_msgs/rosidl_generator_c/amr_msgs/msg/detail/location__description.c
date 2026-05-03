// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from amr_msgs:msg/Location.idl
// generated code does not contain a copyright notice

#include "amr_msgs/msg/detail/location__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
const rosidl_type_hash_t *
amr_msgs__msg__Location__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x58, 0x0d, 0x41, 0xc2, 0x2a, 0xfc, 0xc3, 0x3b,
      0xb0, 0xfb, 0xcf, 0x78, 0xb8, 0x28, 0x3b, 0xe5,
      0xe9, 0x8d, 0x28, 0xc2, 0xe9, 0xc6, 0xed, 0xe4,
      0xea, 0x88, 0x1b, 0xce, 0xbd, 0x34, 0x72, 0x53,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types

// Hashes for external referenced types
#ifndef NDEBUG
#endif

static char amr_msgs__msg__Location__TYPE_NAME[] = "amr_msgs/msg/Location";

// Define type names, field names, and default values
static char amr_msgs__msg__Location__FIELD_NAME__x[] = "x";
static char amr_msgs__msg__Location__FIELD_NAME__y[] = "y";
static char amr_msgs__msg__Location__FIELD_NAME__theta[] = "theta";

static rosidl_runtime_c__type_description__Field amr_msgs__msg__Location__FIELDS[] = {
  {
    {amr_msgs__msg__Location__FIELD_NAME__x, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {amr_msgs__msg__Location__FIELD_NAME__y, 1, 1},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {amr_msgs__msg__Location__FIELD_NAME__theta, 5, 5},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_DOUBLE,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
amr_msgs__msg__Location__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {amr_msgs__msg__Location__TYPE_NAME, 21, 21},
      {amr_msgs__msg__Location__FIELDS, 3, 3},
    },
    {NULL, 0, 0},
  };
  if (!constructed) {
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "# This contains the position of a point in free space\n"
  "float64 x\n"
  "float64 y\n"
  "float64 theta";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
amr_msgs__msg__Location__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {amr_msgs__msg__Location__TYPE_NAME, 21, 21},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 88, 88},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
amr_msgs__msg__Location__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[1];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 1, 1};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *amr_msgs__msg__Location__get_individual_type_description_source(NULL),
    constructed = true;
  }
  return &source_sequence;
}
