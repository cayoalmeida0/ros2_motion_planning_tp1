// generated from rosidl_generator_c/resource/idl__description.c.em
// with input from amr_msgs:msg/Status.idl
// generated code does not contain a copyright notice

#include "amr_msgs/msg/detail/status__functions.h"

ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
const rosidl_type_hash_t *
amr_msgs__msg__Status__get_type_hash(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_type_hash_t hash = {1, {
      0x58, 0x84, 0x10, 0xf7, 0x0a, 0x65, 0xac, 0xaf,
      0x33, 0x10, 0xac, 0x56, 0xd9, 0x8b, 0x6c, 0x91,
      0x25, 0x49, 0x70, 0x19, 0x2a, 0xd1, 0xd7, 0xdc,
      0x83, 0x08, 0x15, 0x86, 0xe2, 0x5b, 0x16, 0x8f,
    }};
  return &hash;
}

#include <assert.h>
#include <string.h>

// Include directives for referenced types
#include "amr_msgs/msg/detail/location__functions.h"

// Hashes for external referenced types
#ifndef NDEBUG
static const rosidl_type_hash_t amr_msgs__msg__Location__EXPECTED_HASH = {1, {
    0x58, 0x0d, 0x41, 0xc2, 0x2a, 0xfc, 0xc3, 0x3b,
    0xb0, 0xfb, 0xcf, 0x78, 0xb8, 0x28, 0x3b, 0xe5,
    0xe9, 0x8d, 0x28, 0xc2, 0xe9, 0xc6, 0xed, 0xe4,
    0xea, 0x88, 0x1b, 0xce, 0xbd, 0x34, 0x72, 0x53,
  }};
#endif

static char amr_msgs__msg__Status__TYPE_NAME[] = "amr_msgs/msg/Status";
static char amr_msgs__msg__Location__TYPE_NAME[] = "amr_msgs/msg/Location";

// Define type names, field names, and default values
static char amr_msgs__msg__Status__FIELD_NAME__extended_status[] = "extended_status";
static char amr_msgs__msg__Status__FIELD_NAME__status[] = "status";
static char amr_msgs__msg__Status__FIELD_NAME__state_of_charge[] = "state_of_charge";
static char amr_msgs__msg__Status__FIELD_NAME__localization_score[] = "localization_score";
static char amr_msgs__msg__Status__FIELD_NAME__temperature[] = "temperature";
static char amr_msgs__msg__Status__FIELD_NAME__location[] = "location";

static rosidl_runtime_c__type_description__Field amr_msgs__msg__Status__FIELDS[] = {
  {
    {amr_msgs__msg__Status__FIELD_NAME__extended_status, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {amr_msgs__msg__Status__FIELD_NAME__status, 6, 6},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_STRING,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {amr_msgs__msg__Status__FIELD_NAME__state_of_charge, 15, 15},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {amr_msgs__msg__Status__FIELD_NAME__localization_score, 18, 18},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {amr_msgs__msg__Status__FIELD_NAME__temperature, 11, 11},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_FLOAT,
      0,
      0,
      {NULL, 0, 0},
    },
    {NULL, 0, 0},
  },
  {
    {amr_msgs__msg__Status__FIELD_NAME__location, 8, 8},
    {
      rosidl_runtime_c__type_description__FieldType__FIELD_TYPE_NESTED_TYPE,
      0,
      0,
      {amr_msgs__msg__Location__TYPE_NAME, 21, 21},
    },
    {NULL, 0, 0},
  },
};

static rosidl_runtime_c__type_description__IndividualTypeDescription amr_msgs__msg__Status__REFERENCED_TYPE_DESCRIPTIONS[] = {
  {
    {amr_msgs__msg__Location__TYPE_NAME, 21, 21},
    {NULL, 0, 0},
  },
};

const rosidl_runtime_c__type_description__TypeDescription *
amr_msgs__msg__Status__get_type_description(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static bool constructed = false;
  static const rosidl_runtime_c__type_description__TypeDescription description = {
    {
      {amr_msgs__msg__Status__TYPE_NAME, 19, 19},
      {amr_msgs__msg__Status__FIELDS, 6, 6},
    },
    {amr_msgs__msg__Status__REFERENCED_TYPE_DESCRIPTIONS, 1, 1},
  };
  if (!constructed) {
    assert(0 == memcmp(&amr_msgs__msg__Location__EXPECTED_HASH, amr_msgs__msg__Location__get_type_hash(NULL), sizeof(rosidl_type_hash_t)));
    description.referenced_type_descriptions.data[0].fields = amr_msgs__msg__Location__get_type_description(NULL)->type_description.fields;
    constructed = true;
  }
  return &description;
}

static char toplevel_type_raw_source[] =
  "string extended_status\n"
  "string status\n"
  "float32 state_of_charge\n"
  "float32 localization_score\n"
  "float32 temperature\n"
  "amr_msgs/Location location";

static char msg_encoding[] = "msg";

// Define all individual source functions

const rosidl_runtime_c__type_description__TypeSource *
amr_msgs__msg__Status__get_individual_type_description_source(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static const rosidl_runtime_c__type_description__TypeSource source = {
    {amr_msgs__msg__Status__TYPE_NAME, 19, 19},
    {msg_encoding, 3, 3},
    {toplevel_type_raw_source, 135, 135},
  };
  return &source;
}

const rosidl_runtime_c__type_description__TypeSource__Sequence *
amr_msgs__msg__Status__get_type_description_sources(
  const rosidl_message_type_support_t * type_support)
{
  (void)type_support;
  static rosidl_runtime_c__type_description__TypeSource sources[2];
  static const rosidl_runtime_c__type_description__TypeSource__Sequence source_sequence = {sources, 2, 2};
  static bool constructed = false;
  if (!constructed) {
    sources[0] = *amr_msgs__msg__Status__get_individual_type_description_source(NULL),
    sources[1] = *amr_msgs__msg__Location__get_individual_type_description_source(NULL);
    constructed = true;
  }
  return &source_sequence;
}
