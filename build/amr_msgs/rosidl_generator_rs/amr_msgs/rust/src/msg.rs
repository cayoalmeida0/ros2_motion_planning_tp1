#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to amr_msgs__msg__Location
/// This contains the position of a point in free space

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Location::default())
  }
}

impl rosidl_runtime_rs::Message for Location {
  type RmwMsg = super::msg::rmw::Location;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        x: msg.x,
        y: msg.y,
        theta: msg.theta,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      x: msg.x,
      y: msg.y,
      theta: msg.theta,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      x: msg.x,
      y: msg.y,
      theta: msg.theta,
    }
  }
}


// Corresponds to amr_msgs__msg__Status

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct Status {

    // This member is not documented.
    #[allow(missing_docs)]
    pub extended_status: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub status: std::string::String,


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
    pub location: super::msg::Location,

}



impl Default for Status {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::Status::default())
  }
}

impl rosidl_runtime_rs::Message for Status {
  type RmwMsg = super::msg::rmw::Status;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        extended_status: msg.extended_status.as_str().into(),
        status: msg.status.as_str().into(),
        state_of_charge: msg.state_of_charge,
        localization_score: msg.localization_score,
        temperature: msg.temperature,
        location: super::msg::Location::into_rmw_message(std::borrow::Cow::Owned(msg.location)).into_owned(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        extended_status: msg.extended_status.as_str().into(),
        status: msg.status.as_str().into(),
      state_of_charge: msg.state_of_charge,
      localization_score: msg.localization_score,
      temperature: msg.temperature,
        location: super::msg::Location::into_rmw_message(std::borrow::Cow::Borrowed(&msg.location)).into_owned(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      extended_status: msg.extended_status.to_string(),
      status: msg.status.to_string(),
      state_of_charge: msg.state_of_charge,
      localization_score: msg.localization_score,
      temperature: msg.temperature,
      location: super::msg::Location::from_rmw_message(msg.location),
    }
  }
}


