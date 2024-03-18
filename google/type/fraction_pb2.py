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
# source: google/type/fraction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x1agoogle/type/fraction.proto\x12\x0bgoogle.type"2\n\x08\x46raction\x12\x11\n\tnumerator\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x65nominator\x18\x02 \x01(\x03\x42\x66\n\x0f\x63om.google.typeB\rFractionProtoP\x01Z<google.golang.org/genproto/googleapis/type/fraction;fraction\xa2\x02\x03GTPb\x06proto3'
)


_FRACTION = DESCRIPTOR.message_types_by_name["Fraction"]
Fraction = _reflection.GeneratedProtocolMessageType(
    "Fraction",
    (_message.Message,),
    {
        "DESCRIPTOR": _FRACTION,
        "__module__": "google.type.fraction_pb2"
        # @@protoc_insertion_point(class_scope:google.type.Fraction)
    },
)
_sym_db.RegisterMessage(Fraction)

if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\017com.google.typeB\rFractionProtoP\001Z<google.golang.org/genproto/googleapis/type/fraction;fraction\242\002\003GTP"
    _FRACTION._serialized_start = 43
    _FRACTION._serialized_end = 93
# @@protoc_insertion_point(module_scope)
