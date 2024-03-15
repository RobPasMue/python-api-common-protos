# -*- coding: utf-8 -*-

# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/api/field_info.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1bgoogle/api/field_info.proto\x12\ngoogle.api\x1a google/protobuf/descriptor.proto"\x8c\x01\n\tFieldInfo\x12,\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x1c.google.api.FieldInfo.Format"Q\n\x06\x46ormat\x12\x16\n\x12\x46ORMAT_UNSPECIFIED\x10\x00\x12\t\n\x05UUID4\x10\x01\x12\x08\n\x04IPV4\x10\x02\x12\x08\n\x04IPV6\x10\x03\x12\x10\n\x0cIPV4_OR_IPV6\x10\x04:L\n\nfield_info\x12\x1d.google.protobuf.FieldOptions\x18\xcc\xf1\xf9\x8a\x01 \x01(\x0b\x32\x15.google.api.FieldInfoBl\n\x0e\x63om.google.apiB\x0e\x46ieldInfoProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3'
)


FIELD_INFO_FIELD_NUMBER = 291403980
field_info = DESCRIPTOR.extensions_by_name["field_info"]

_FIELDINFO = DESCRIPTOR.message_types_by_name["FieldInfo"]
_FIELDINFO_FORMAT = _FIELDINFO.enum_types_by_name["Format"]
FieldInfo = _reflection.GeneratedProtocolMessageType(
    "FieldInfo",
    (_message.Message,),
    {
        "DESCRIPTOR": _FIELDINFO,
        "__module__": "google.api.field_info_pb2"
        # @@protoc_insertion_point(class_scope:google.api.FieldInfo)
    },
)
_sym_db.RegisterMessage(FieldInfo)

if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(field_info)

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\016FieldInfoProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI"
    _FIELDINFO._serialized_start = 78
    _FIELDINFO._serialized_end = 218
    _FIELDINFO_FORMAT._serialized_start = 137
    _FIELDINFO_FORMAT._serialized_end = 218
# @@protoc_insertion_point(module_scope)
