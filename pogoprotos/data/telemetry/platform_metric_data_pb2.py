# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/data/telemetry/platform_metric_data.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.telemetry import distribution_pb2 as pogoprotos_dot_data_dot_telemetry_dot_distribution__pb2
from pogoprotos.data.telemetry import telemetry_common_pb2 as pogoprotos_dot_data_dot_telemetry_dot_telemetry__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/data/telemetry/platform_metric_data.proto',
  package='pogoprotos.data.telemetry',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n4pogoprotos/data/telemetry/platform_metric_data.proto\x12\x19pogoprotos.data.telemetry\x1a,pogoprotos/data/telemetry/distribution.proto\x1a\x30pogoprotos/data/telemetry/telemetry_common.proto\"\xfc\x02\n\x12PlatformMetricData\x12\x44\n\x10\x63ommon_telemetry\x18\x01 \x01(\x0b\x32*.pogoprotos.data.telemetry.TelemetryCommon\x12\x14\n\nlong_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0c\x64ouble_value\x18\x03 \x01(\x01H\x00\x12\x17\n\rboolean_value\x18\x04 \x01(\x08H\x00\x12?\n\x0c\x64istribution\x18\x05 \x01(\x0b\x32\'.pogoprotos.data.telemetry.DistributionH\x00\x12G\n\x0bmetric_kind\x18\x06 \x01(\x0e\x32\x32.pogoprotos.data.telemetry.PlatformMetricData.Kind\"=\n\x04Kind\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05GAUGE\x10\x01\x12\t\n\x05\x44\x45LTA\x10\x02\x12\x0e\n\nCUMULATIVE\x10\x03\x42\x10\n\x0e\x44\x61tapointValueb\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_telemetry_dot_distribution__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_telemetry_dot_telemetry__common__pb2.DESCRIPTOR,])



_PLATFORMMETRICDATA_KIND = _descriptor.EnumDescriptor(
  name='Kind',
  full_name='pogoprotos.data.telemetry.PlatformMetricData.Kind',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSPECIFIED', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GAUGE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELTA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUMULATIVE', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=481,
  serialized_end=542,
)
_sym_db.RegisterEnumDescriptor(_PLATFORMMETRICDATA_KIND)


_PLATFORMMETRICDATA = _descriptor.Descriptor(
  name='PlatformMetricData',
  full_name='pogoprotos.data.telemetry.PlatformMetricData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common_telemetry', full_name='pogoprotos.data.telemetry.PlatformMetricData.common_telemetry', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='long_value', full_name='pogoprotos.data.telemetry.PlatformMetricData.long_value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='double_value', full_name='pogoprotos.data.telemetry.PlatformMetricData.double_value', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='boolean_value', full_name='pogoprotos.data.telemetry.PlatformMetricData.boolean_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='distribution', full_name='pogoprotos.data.telemetry.PlatformMetricData.distribution', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='metric_kind', full_name='pogoprotos.data.telemetry.PlatformMetricData.metric_kind', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PLATFORMMETRICDATA_KIND,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='DatapointValue', full_name='pogoprotos.data.telemetry.PlatformMetricData.DatapointValue',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=180,
  serialized_end=560,
)

_PLATFORMMETRICDATA.fields_by_name['common_telemetry'].message_type = pogoprotos_dot_data_dot_telemetry_dot_telemetry__common__pb2._TELEMETRYCOMMON
_PLATFORMMETRICDATA.fields_by_name['distribution'].message_type = pogoprotos_dot_data_dot_telemetry_dot_distribution__pb2._DISTRIBUTION
_PLATFORMMETRICDATA.fields_by_name['metric_kind'].enum_type = _PLATFORMMETRICDATA_KIND
_PLATFORMMETRICDATA_KIND.containing_type = _PLATFORMMETRICDATA
_PLATFORMMETRICDATA.oneofs_by_name['DatapointValue'].fields.append(
  _PLATFORMMETRICDATA.fields_by_name['long_value'])
_PLATFORMMETRICDATA.fields_by_name['long_value'].containing_oneof = _PLATFORMMETRICDATA.oneofs_by_name['DatapointValue']
_PLATFORMMETRICDATA.oneofs_by_name['DatapointValue'].fields.append(
  _PLATFORMMETRICDATA.fields_by_name['double_value'])
_PLATFORMMETRICDATA.fields_by_name['double_value'].containing_oneof = _PLATFORMMETRICDATA.oneofs_by_name['DatapointValue']
_PLATFORMMETRICDATA.oneofs_by_name['DatapointValue'].fields.append(
  _PLATFORMMETRICDATA.fields_by_name['boolean_value'])
_PLATFORMMETRICDATA.fields_by_name['boolean_value'].containing_oneof = _PLATFORMMETRICDATA.oneofs_by_name['DatapointValue']
_PLATFORMMETRICDATA.oneofs_by_name['DatapointValue'].fields.append(
  _PLATFORMMETRICDATA.fields_by_name['distribution'])
_PLATFORMMETRICDATA.fields_by_name['distribution'].containing_oneof = _PLATFORMMETRICDATA.oneofs_by_name['DatapointValue']
DESCRIPTOR.message_types_by_name['PlatformMetricData'] = _PLATFORMMETRICDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PlatformMetricData = _reflection.GeneratedProtocolMessageType('PlatformMetricData', (_message.Message,), dict(
  DESCRIPTOR = _PLATFORMMETRICDATA,
  __module__ = 'pogoprotos.data.telemetry.platform_metric_data_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.data.telemetry.PlatformMetricData)
  ))
_sym_db.RegisterMessage(PlatformMetricData)


# @@protoc_insertion_point(module_scope)