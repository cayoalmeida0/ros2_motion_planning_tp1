#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__Location() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__Location__init(msg: *mut Location) -> bool;
    fn amr_msgs__msg__Location__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Location>, size: usize) -> bool;
    fn amr_msgs__msg__Location__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Location>);
    fn amr_msgs__msg__Location__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Location>, out_seq: *mut rosidl_runtime_rs::Sequence<Location>) -> bool;
}

// Corresponds to amr_msgs__msg__Location
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// This contains the position of a point in free space

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Location {

    // This member is not documented.
    #[allow(missing_docs)]
    pub x: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub y: f64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub theta: f64,

}



impl Default for Location {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__Location__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__Location__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Location {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__Location__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__Location__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__Location__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Location {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Location where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/Location";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__Location() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__Status() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__Status__init(msg: *mut Status) -> bool;
    fn amr_msgs__msg__Status__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<Status>, size: usize) -> bool;
    fn amr_msgs__msg__Status__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<Status>);
    fn amr_msgs__msg__Status__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<Status>, out_seq: *mut rosidl_runtime_rs::Sequence<Status>) -> bool;
}

// Corresponds to amr_msgs__msg__Status
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Status {

    // This member is not documented.
    #[allow(missing_docs)]
    pub extended_status: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub status: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub state_of_charge: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub localization_score: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub temperature: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub location: super::super::msg::rmw::Location,

}



impl Default for Status {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__Status__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__Status__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for Status {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__Status__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__Status__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__Status__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for Status {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for Status where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/Status";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__Status() }
  }
}


