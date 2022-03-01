# -*- coding: utf-8 -*-

# Copyright 2020 Google LLC
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
# source: google/api/documentation.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1egoogle/api/documentation.proto\x12\ngoogle.api"\xa1\x01\n\rDocumentation\x12\x0f\n\x07summary\x18\x01 \x01(\t\x12\x1f\n\x05pages\x18\x05 \x03(\x0b\x32\x10.google.api.Page\x12,\n\x05rules\x18\x03 \x03(\x0b\x32\x1d.google.api.DocumentationRule\x12\x1e\n\x16\x64ocumentation_root_url\x18\x04 \x01(\t\x12\x10\n\x08overview\x18\x02 \x01(\t"[\n\x11\x44ocumentationRule\x12\x10\n\x08selector\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1f\n\x17\x64\x65precation_description\x18\x03 \x01(\t"I\n\x04Page\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12"\n\x08subpages\x18\x03 \x03(\x0b\x32\x10.google.api.PageBt\n\x0e\x63om.google.apiB\x12\x44ocumentationProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\xa2\x02\x04GAPIb\x06proto3'
)


_DOCUMENTATION = DESCRIPTOR.message_types_by_name["Documentation"]
_DOCUMENTATIONRULE = DESCRIPTOR.message_types_by_name["DocumentationRule"]
_PAGE = DESCRIPTOR.message_types_by_name["Page"]
Documentation = _reflection.GeneratedProtocolMessageType(
    "Documentation",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOCUMENTATION,
        "__module__": "google.api.documentation_pb2"
        # @@protoc_insertion_point(class_scope:google.api.Documentation)
    },
)
_sym_db.RegisterMessage(Documentation)

DocumentationRule = _reflection.GeneratedProtocolMessageType(
    "DocumentationRule",
    (_message.Message,),
    {
        "DESCRIPTOR": _DOCUMENTATIONRULE,
        "__module__": "google.api.documentation_pb2"
        # @@protoc_insertion_point(class_scope:google.api.DocumentationRule)
    },
)
_sym_db.RegisterMessage(DocumentationRule)

Page = _reflection.GeneratedProtocolMessageType(
    "Page",
    (_message.Message,),
    {
        "DESCRIPTOR": _PAGE,
        "__module__": "google.api.documentation_pb2"
        # @@protoc_insertion_point(class_scope:google.api.Page)
    },
)
_sym_db.RegisterMessage(Page)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\022DocumentationProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig\242\002\004GAPI"
    _DOCUMENTATION._serialized_start = 47
    _DOCUMENTATION._serialized_end = 208
    _DOCUMENTATIONRULE._serialized_start = 210
    _DOCUMENTATIONRULE._serialized_end = 301
    _PAGE._serialized_start = 303
    _PAGE._serialized_end = 376
# @@protoc_insertion_point(module_scope)
