# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/enums/incubation_result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/enums/incubation_result.proto',
  package='pogoprotos.enums',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/enums/incubation_result.proto\x12\x10pogoprotos.enums*>\n\x10IncubationResult\x12\x1d\n\x19SUCCESS_INCUBATION_RESULT\x10\x00\x12\x0b\n\x07\x46\x41ILURE\x10\x01\x62\x06proto3')
)

_INCUBATIONRESULT = _descriptor.EnumDescriptor(
  name='IncubationResult',
  full_name='pogoprotos.enums.IncubationResult',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SUCCESS_INCUBATION_RESULT', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILURE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=62,
  serialized_end=124,
)
_sym_db.RegisterEnumDescriptor(_INCUBATIONRESULT)

IncubationResult = enum_type_wrapper.EnumTypeWrapper(_INCUBATIONRESULT)
SUCCESS_INCUBATION_RESULT = 0
FAILURE = 1


DESCRIPTOR.enum_types_by_name['IncubationResult'] = _INCUBATIONRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
