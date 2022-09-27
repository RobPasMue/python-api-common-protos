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
# source: google/api/consumer.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x19google/api/consumer.proto\x12\ngoogle.api"=\n\x11ProjectProperties\x12(\n\nproperties\x18\x01 \x03(\x0b\x32\x14.google.api.Property"\xac\x01\n\x08Property\x12\x0c\n\x04name\x18\x01 \x01(\t\x12/\n\x04type\x18\x02 \x01(\x0e\x32!.google.api.Property.PropertyType\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t"L\n\x0cPropertyType\x12\x0f\n\x0bUNSPECIFIED\x10\x00\x12\t\n\x05INT64\x10\x01\x12\x08\n\x04\x42OOL\x10\x02\x12\n\n\x06STRING\x10\x03\x12\n\n\x06\x44OUBLE\x10\x04\x42h\n\x0e\x63om.google.apiB\rConsumerProtoP\x01ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfigb\x06proto3'
)

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(
    DESCRIPTOR, "google.api.consumer_pb2", globals()
)
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\rConsumerProtoP\001ZEgoogle.golang.org/genproto/googleapis/api/serviceconfig;serviceconfig"
    _PROJECTPROPERTIES._serialized_start = 41
    _PROJECTPROPERTIES._serialized_end = 102
    _PROPERTY._serialized_start = 105
    _PROPERTY._serialized_end = 277
    _PROPERTY_PROPERTYTYPE._serialized_start = 201
    _PROPERTY_PROPERTYTYPE._serialized_end = 277
# @@protoc_insertion_point(module_scope)
