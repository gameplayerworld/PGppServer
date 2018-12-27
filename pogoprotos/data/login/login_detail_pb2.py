# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/login/login_detail.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import identity_provider_pb2 as pogoprotos_dot_enums_dot_identity__provider__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/login/login_detail.proto',
  package='pogoprotos.data.login',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n(pogoprotos/data/login/login_detail.proto\x12\x15pogoprotos.data.login\x1a(pogoprotos/enums/identity_provider.proto\"[\n\x0bLoginDetail\x12=\n\x11identity_provider\x18\x01 \x01(\x0e\x32\".pogoprotos.enums.IdentityProvider\x12\r\n\x05\x65mail\x18\x02 \x01(\tb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_identity__provider__pb2.DESCRIPTOR,])




_LOGINDETAIL = _descriptor.Descriptor(
  name='LoginDetail',
  full_name='pogoprotos.data.login.LoginDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity_provider', full_name='pogoprotos.data.login.LoginDetail.identity_provider', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='pogoprotos.data.login.LoginDetail.email', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=200,
)

_LOGINDETAIL.fields_by_name['identity_provider'].enum_type = pogoprotos_dot_enums_dot_identity__provider__pb2._IDENTITYPROVIDER
DESCRIPTOR.message_types_by_name['LoginDetail'] = _LOGINDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LoginDetail = _reflection.GeneratedProtocolMessageType('LoginDetail', (_message.Message,), dict(
  DESCRIPTOR = _LOGINDETAIL,
  __module__ = 'pogoprotos.data.login.login_detail_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.login.LoginDetail)
  ))
_sym_db.RegisterMessage(LoginDetail)


# @@protoc_insertion_point(module_scope)
