# generated from rosidl_generator_py/resource/_idl.py.em
# with input from amr_msgs:msg/Status.idl
# generated code does not contain a copyright notice

# This is being done at the module level and not on the instance level to avoid looking
# for the same variable multiple times on each instance. This variable is not supposed to
# change during runtime so it makes sense to only look for it once.
from os import getenv

ros_python_check_fields = getenv('ROS_PYTHON_CHECK_FIELDS', default='')


# Import statements for member types

import builtins  # noqa: E402, I100

import math  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_Status(type):
    """Metaclass of message 'Status'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('amr_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'amr_msgs.msg.Status')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__status
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__status
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__status
            cls._TYPE_SUPPORT = module.type_support_msg__msg__status
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__status

            from amr_msgs.msg import Location
            if Location.__class__._TYPE_SUPPORT is None:
                Location.__class__.__import_type_support__()

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class Status(metaclass=Metaclass_Status):
    """Message class 'Status'."""

    __slots__ = [
        '_extended_status',
        '_status',
        '_state_of_charge',
        '_localization_score',
        '_temperature',
        '_location',
        '_check_fields',
    ]

    _fields_and_field_types = {
        'extended_status': 'string',
        'status': 'string',
        'state_of_charge': 'float',
        'localization_score': 'float',
        'temperature': 'float',
        'location': 'amr_msgs/Location',
    }

    # This attribute is used to store an rosidl_parser.definition variable
    # related to the data type of each of the components the message.
    SLOT_TYPES = (
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.UnboundedString(),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.NamespacedType(['amr_msgs', 'msg'], 'Location'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        if 'check_fields' in kwargs:
            self._check_fields = kwargs['check_fields']
        else:
            self._check_fields = ros_python_check_fields == '1'
        if self._check_fields:
            assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
                'Invalid arguments passed to constructor: %s' % \
                ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.extended_status = kwargs.get('extended_status', str())
        self.status = kwargs.get('status', str())
        self.state_of_charge = kwargs.get('state_of_charge', float())
        self.localization_score = kwargs.get('localization_score', float())
        self.temperature = kwargs.get('temperature', float())
        from amr_msgs.msg import Location
        self.location = kwargs.get('location', Location())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.get_fields_and_field_types().keys(), self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    if self._check_fields:
                        assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.extended_status != other.extended_status:
            return False
        if self.status != other.status:
            return False
        if self.state_of_charge != other.state_of_charge:
            return False
        if self.localization_score != other.localization_score:
            return False
        if self.temperature != other.temperature:
            return False
        if self.location != other.location:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def extended_status(self):
        """Message field 'extended_status'."""
        return self._extended_status

    @extended_status.setter
    def extended_status(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'extended_status' field must be of type 'str'"
        self._extended_status = value

    @builtins.property
    def status(self):
        """Message field 'status'."""
        return self._status

    @status.setter
    def status(self, value):
        if self._check_fields:
            assert \
                isinstance(value, str), \
                "The 'status' field must be of type 'str'"
        self._status = value

    @builtins.property
    def state_of_charge(self):
        """Message field 'state_of_charge'."""
        return self._state_of_charge

    @state_of_charge.setter
    def state_of_charge(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'state_of_charge' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'state_of_charge' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._state_of_charge = value

    @builtins.property
    def localization_score(self):
        """Message field 'localization_score'."""
        return self._localization_score

    @localization_score.setter
    def localization_score(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'localization_score' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'localization_score' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._localization_score = value

    @builtins.property
    def temperature(self):
        """Message field 'temperature'."""
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if self._check_fields:
            assert \
                isinstance(value, float), \
                "The 'temperature' field must be of type 'float'"
            assert not (value < -3.402823466e+38 or value > 3.402823466e+38) or math.isinf(value), \
                "The 'temperature' field must be a float in [-3.402823466e+38, 3.402823466e+38]"
        self._temperature = value

    @builtins.property
    def location(self):
        """Message field 'location'."""
        return self._location

    @location.setter
    def location(self, value):
        if self._check_fields:
            from amr_msgs.msg import Location
            assert \
                isinstance(value, Location), \
                "The 'location' field must be a sub message of type 'Location'"
        self._location = value
