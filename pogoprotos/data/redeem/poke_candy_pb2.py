# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/redeem/poke_candy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/redeem/poke_candy.proto',
  package='pogoprotos.data.redeem',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'pogoprotos/data/redeem/poke_candy.proto\x12\x16pogoprotos.data.redeem\"4\n\tPokeCandy\x12\x12\n\npokemon_id\x18\x01 \x01(\x06\x12\x13\n\x0b\x63\x61ndy_count\x18\x02 \x01(\x05\x62\x06proto3')
)




_POKECANDY = _descriptor.Descriptor(
  name='PokeCandy',
  full_name='pogoprotos.data.redeem.PokeCandy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='pogoprotos.data.redeem.PokeCandy.pokemon_id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='candy_count', full_name='pogoprotos.data.redeem.PokeCandy.candy_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=67,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['PokeCandy'] = _POKECANDY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PokeCandy = _reflection.GeneratedProtocolMessageType('PokeCandy', (_message.Message,), dict(
  DESCRIPTOR = _POKECANDY,
  __module__ = 'pogoprotos.data.redeem.poke_candy_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.redeem.PokeCandy)
  ))
_sym_db.RegisterMessage(PokeCandy)


# @@protoc_insertion_point(module_scope)
