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
# source: google/api/client.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import launch_stage_pb2 as google_dot_api_dot_launch__stage__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x17google/api/client.proto\x12\ngoogle.api\x1a\x1dgoogle/api/launch_stage.proto\x1a google/protobuf/descriptor.proto\x1a\x1egoogle/protobuf/duration.proto"t\n\x16\x43ommonLanguageSettings\x12\x1e\n\x12reference_docs_uri\x18\x01 \x01(\tB\x02\x18\x01\x12:\n\x0c\x64\x65stinations\x18\x02 \x03(\x0e\x32$.google.api.ClientLibraryDestination"\xfb\x03\n\x15\x43lientLibrarySettings\x12\x0f\n\x07version\x18\x01 \x01(\t\x12-\n\x0claunch_stage\x18\x02 \x01(\x0e\x32\x17.google.api.LaunchStage\x12\x1a\n\x12rest_numeric_enums\x18\x03 \x01(\x08\x12/\n\rjava_settings\x18\x15 \x01(\x0b\x32\x18.google.api.JavaSettings\x12-\n\x0c\x63pp_settings\x18\x16 \x01(\x0b\x32\x17.google.api.CppSettings\x12-\n\x0cphp_settings\x18\x17 \x01(\x0b\x32\x17.google.api.PhpSettings\x12\x33\n\x0fpython_settings\x18\x18 \x01(\x0b\x32\x1a.google.api.PythonSettings\x12/\n\rnode_settings\x18\x19 \x01(\x0b\x32\x18.google.api.NodeSettings\x12\x33\n\x0f\x64otnet_settings\x18\x1a \x01(\x0b\x32\x1a.google.api.DotnetSettings\x12/\n\rruby_settings\x18\x1b \x01(\x0b\x32\x18.google.api.RubySettings\x12+\n\x0bgo_settings\x18\x1c \x01(\x0b\x32\x16.google.api.GoSettings"\xa8\x03\n\nPublishing\x12\x33\n\x0fmethod_settings\x18\x02 \x03(\x0b\x32\x1a.google.api.MethodSettings\x12\x15\n\rnew_issue_uri\x18\x65 \x01(\t\x12\x19\n\x11\x64ocumentation_uri\x18\x66 \x01(\t\x12\x16\n\x0e\x61pi_short_name\x18g \x01(\t\x12\x14\n\x0cgithub_label\x18h \x01(\t\x12\x1e\n\x16\x63odeowner_github_teams\x18i \x03(\t\x12\x16\n\x0e\x64oc_tag_prefix\x18j \x01(\t\x12;\n\x0corganization\x18k \x01(\x0e\x32%.google.api.ClientLibraryOrganization\x12;\n\x10library_settings\x18m \x03(\x0b\x32!.google.api.ClientLibrarySettings\x12)\n!proto_reference_documentation_uri\x18n \x01(\t\x12(\n rest_reference_documentation_uri\x18o \x01(\t"\xe3\x01\n\x0cJavaSettings\x12\x17\n\x0flibrary_package\x18\x01 \x01(\t\x12L\n\x13service_class_names\x18\x02 \x03(\x0b\x32/.google.api.JavaSettings.ServiceClassNamesEntry\x12\x32\n\x06\x63ommon\x18\x03 \x01(\x0b\x32".google.api.CommonLanguageSettings\x1a\x38\n\x16ServiceClassNamesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"A\n\x0b\x43ppSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"A\n\x0bPhpSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"D\n\x0ePythonSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"B\n\x0cNodeSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"\xaa\x03\n\x0e\x44otnetSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings\x12I\n\x10renamed_services\x18\x02 \x03(\x0b\x32/.google.api.DotnetSettings.RenamedServicesEntry\x12K\n\x11renamed_resources\x18\x03 \x03(\x0b\x32\x30.google.api.DotnetSettings.RenamedResourcesEntry\x12\x19\n\x11ignored_resources\x18\x04 \x03(\t\x12 \n\x18\x66orced_namespace_aliases\x18\x05 \x03(\t\x12\x1e\n\x16handwritten_signatures\x18\x06 \x03(\t\x1a\x36\n\x14RenamedServicesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15RenamedResourcesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01"B\n\x0cRubySettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"@\n\nGoSettings\x12\x32\n\x06\x63ommon\x18\x01 \x01(\x0b\x32".google.api.CommonLanguageSettings"\xcf\x02\n\x0eMethodSettings\x12\x10\n\x08selector\x18\x01 \x01(\t\x12<\n\x0clong_running\x18\x02 \x01(\x0b\x32&.google.api.MethodSettings.LongRunning\x12\x1d\n\x15\x61uto_populated_fields\x18\x03 \x03(\t\x1a\xcd\x01\n\x0bLongRunning\x12\x35\n\x12initial_poll_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x1d\n\x15poll_delay_multiplier\x18\x02 \x01(\x02\x12\x31\n\x0emax_poll_delay\x18\x03 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x35\n\x12total_poll_timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration*\xa3\x01\n\x19\x43lientLibraryOrganization\x12+\n\'CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED\x10\x00\x12\t\n\x05\x43LOUD\x10\x01\x12\x07\n\x03\x41\x44S\x10\x02\x12\n\n\x06PHOTOS\x10\x03\x12\x0f\n\x0bSTREET_VIEW\x10\x04\x12\x0c\n\x08SHOPPING\x10\x05\x12\x07\n\x03GEO\x10\x06\x12\x11\n\rGENERATIVE_AI\x10\x07*g\n\x18\x43lientLibraryDestination\x12*\n&CLIENT_LIBRARY_DESTINATION_UNSPECIFIED\x10\x00\x12\n\n\x06GITHUB\x10\n\x12\x13\n\x0fPACKAGE_MANAGER\x10\x14:9\n\x10method_signature\x12\x1e.google.protobuf.MethodOptions\x18\x9b\x08 \x03(\t:6\n\x0c\x64\x65\x66\x61ult_host\x12\x1f.google.protobuf.ServiceOptions\x18\x99\x08 \x01(\t:6\n\x0coauth_scopes\x12\x1f.google.protobuf.ServiceOptions\x18\x9a\x08 \x01(\t:8\n\x0b\x61pi_version\x12\x1f.google.protobuf.ServiceOptions\x18\xc1\xba\xab\xfa\x01 \x01(\tBi\n\x0e\x63om.google.apiB\x0b\x43lientProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3'
)

_CLIENTLIBRARYORGANIZATION = DESCRIPTOR.enum_types_by_name["ClientLibraryOrganization"]
ClientLibraryOrganization = enum_type_wrapper.EnumTypeWrapper(
    _CLIENTLIBRARYORGANIZATION
)
_CLIENTLIBRARYDESTINATION = DESCRIPTOR.enum_types_by_name["ClientLibraryDestination"]
ClientLibraryDestination = enum_type_wrapper.EnumTypeWrapper(_CLIENTLIBRARYDESTINATION)
CLIENT_LIBRARY_ORGANIZATION_UNSPECIFIED = 0
CLOUD = 1
ADS = 2
PHOTOS = 3
STREET_VIEW = 4
SHOPPING = 5
GEO = 6
GENERATIVE_AI = 7
CLIENT_LIBRARY_DESTINATION_UNSPECIFIED = 0
GITHUB = 10
PACKAGE_MANAGER = 20

METHOD_SIGNATURE_FIELD_NUMBER = 1051
method_signature = DESCRIPTOR.extensions_by_name["method_signature"]
DEFAULT_HOST_FIELD_NUMBER = 1049
default_host = DESCRIPTOR.extensions_by_name["default_host"]
OAUTH_SCOPES_FIELD_NUMBER = 1050
oauth_scopes = DESCRIPTOR.extensions_by_name["oauth_scopes"]
API_VERSION_FIELD_NUMBER = 525000001
api_version = DESCRIPTOR.extensions_by_name["api_version"]

_COMMONLANGUAGESETTINGS = DESCRIPTOR.message_types_by_name["CommonLanguageSettings"]
_CLIENTLIBRARYSETTINGS = DESCRIPTOR.message_types_by_name["ClientLibrarySettings"]
_PUBLISHING = DESCRIPTOR.message_types_by_name["Publishing"]
_JAVASETTINGS = DESCRIPTOR.message_types_by_name["JavaSettings"]
_JAVASETTINGS_SERVICECLASSNAMESENTRY = _JAVASETTINGS.nested_types_by_name[
    "ServiceClassNamesEntry"
]
_CPPSETTINGS = DESCRIPTOR.message_types_by_name["CppSettings"]
_PHPSETTINGS = DESCRIPTOR.message_types_by_name["PhpSettings"]
_PYTHONSETTINGS = DESCRIPTOR.message_types_by_name["PythonSettings"]
_NODESETTINGS = DESCRIPTOR.message_types_by_name["NodeSettings"]
_DOTNETSETTINGS = DESCRIPTOR.message_types_by_name["DotnetSettings"]
_DOTNETSETTINGS_RENAMEDSERVICESENTRY = _DOTNETSETTINGS.nested_types_by_name[
    "RenamedServicesEntry"
]
_DOTNETSETTINGS_RENAMEDRESOURCESENTRY = _DOTNETSETTINGS.nested_types_by_name[
    "RenamedResourcesEntry"
]
_RUBYSETTINGS = DESCRIPTOR.message_types_by_name["RubySettings"]
_GOSETTINGS = DESCRIPTOR.message_types_by_name["GoSettings"]
_METHODSETTINGS = DESCRIPTOR.message_types_by_name["MethodSettings"]
_METHODSETTINGS_LONGRUNNING = _METHODSETTINGS.nested_types_by_name["LongRunning"]
CommonLanguageSettings = _reflection.GeneratedProtocolMessageType(
    "CommonLanguageSettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _COMMONLANGUAGESETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.CommonLanguageSettings)
    },
)
_sym_db.RegisterMessage(CommonLanguageSettings)

ClientLibrarySettings = _reflection.GeneratedProtocolMessageType(
    "ClientLibrarySettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _CLIENTLIBRARYSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.ClientLibrarySettings)
    },
)
_sym_db.RegisterMessage(ClientLibrarySettings)

Publishing = _reflection.GeneratedProtocolMessageType(
    "Publishing",
    (_message.Message,),
    {
        "DESCRIPTOR": _PUBLISHING,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.Publishing)
    },
)
_sym_db.RegisterMessage(Publishing)

JavaSettings = _reflection.GeneratedProtocolMessageType(
    "JavaSettings",
    (_message.Message,),
    {
        "ServiceClassNamesEntry": _reflection.GeneratedProtocolMessageType(
            "ServiceClassNamesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _JAVASETTINGS_SERVICECLASSNAMESENTRY,
                "__module__": "google.api.client_pb2"
                # @@protoc_insertion_point(class_scope:google.api.JavaSettings.ServiceClassNamesEntry)
            },
        ),
        "DESCRIPTOR": _JAVASETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.JavaSettings)
    },
)
_sym_db.RegisterMessage(JavaSettings)
_sym_db.RegisterMessage(JavaSettings.ServiceClassNamesEntry)

CppSettings = _reflection.GeneratedProtocolMessageType(
    "CppSettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _CPPSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.CppSettings)
    },
)
_sym_db.RegisterMessage(CppSettings)

PhpSettings = _reflection.GeneratedProtocolMessageType(
    "PhpSettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _PHPSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.PhpSettings)
    },
)
_sym_db.RegisterMessage(PhpSettings)

PythonSettings = _reflection.GeneratedProtocolMessageType(
    "PythonSettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _PYTHONSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.PythonSettings)
    },
)
_sym_db.RegisterMessage(PythonSettings)

NodeSettings = _reflection.GeneratedProtocolMessageType(
    "NodeSettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _NODESETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.NodeSettings)
    },
)
_sym_db.RegisterMessage(NodeSettings)

DotnetSettings = _reflection.GeneratedProtocolMessageType(
    "DotnetSettings",
    (_message.Message,),
    {
        "RenamedServicesEntry": _reflection.GeneratedProtocolMessageType(
            "RenamedServicesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _DOTNETSETTINGS_RENAMEDSERVICESENTRY,
                "__module__": "google.api.client_pb2"
                # @@protoc_insertion_point(class_scope:google.api.DotnetSettings.RenamedServicesEntry)
            },
        ),
        "RenamedResourcesEntry": _reflection.GeneratedProtocolMessageType(
            "RenamedResourcesEntry",
            (_message.Message,),
            {
                "DESCRIPTOR": _DOTNETSETTINGS_RENAMEDRESOURCESENTRY,
                "__module__": "google.api.client_pb2"
                # @@protoc_insertion_point(class_scope:google.api.DotnetSettings.RenamedResourcesEntry)
            },
        ),
        "DESCRIPTOR": _DOTNETSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.DotnetSettings)
    },
)
_sym_db.RegisterMessage(DotnetSettings)
_sym_db.RegisterMessage(DotnetSettings.RenamedServicesEntry)
_sym_db.RegisterMessage(DotnetSettings.RenamedResourcesEntry)

RubySettings = _reflection.GeneratedProtocolMessageType(
    "RubySettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _RUBYSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.RubySettings)
    },
)
_sym_db.RegisterMessage(RubySettings)

GoSettings = _reflection.GeneratedProtocolMessageType(
    "GoSettings",
    (_message.Message,),
    {
        "DESCRIPTOR": _GOSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.GoSettings)
    },
)
_sym_db.RegisterMessage(GoSettings)

MethodSettings = _reflection.GeneratedProtocolMessageType(
    "MethodSettings",
    (_message.Message,),
    {
        "LongRunning": _reflection.GeneratedProtocolMessageType(
            "LongRunning",
            (_message.Message,),
            {
                "DESCRIPTOR": _METHODSETTINGS_LONGRUNNING,
                "__module__": "google.api.client_pb2"
                # @@protoc_insertion_point(class_scope:google.api.MethodSettings.LongRunning)
            },
        ),
        "DESCRIPTOR": _METHODSETTINGS,
        "__module__": "google.api.client_pb2"
        # @@protoc_insertion_point(class_scope:google.api.MethodSettings)
    },
)
_sym_db.RegisterMessage(MethodSettings)
_sym_db.RegisterMessage(MethodSettings.LongRunning)

if _descriptor._USE_C_DESCRIPTORS == False:
    google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(
        method_signature
    )
    google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(
        default_host
    )
    google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(
        oauth_scopes
    )
    google_dot_protobuf_dot_descriptor__pb2.ServiceOptions.RegisterExtension(
        api_version
    )

    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b"\n\016com.google.apiB\013ClientProtoP\001ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\242\002\004GAPI"
    _COMMONLANGUAGESETTINGS.fields_by_name["reference_docs_uri"]._options = None
    _COMMONLANGUAGESETTINGS.fields_by_name[
        "reference_docs_uri"
    ]._serialized_options = b"\030\001"
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._options = None
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._serialized_options = b"8\001"
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._options = None
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._serialized_options = b"8\001"
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._options = None
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._serialized_options = b"8\001"
    _CLIENTLIBRARYORGANIZATION._serialized_start = 2595
    _CLIENTLIBRARYORGANIZATION._serialized_end = 2758
    _CLIENTLIBRARYDESTINATION._serialized_start = 2760
    _CLIENTLIBRARYDESTINATION._serialized_end = 2863
    _COMMONLANGUAGESETTINGS._serialized_start = 136
    _COMMONLANGUAGESETTINGS._serialized_end = 252
    _CLIENTLIBRARYSETTINGS._serialized_start = 255
    _CLIENTLIBRARYSETTINGS._serialized_end = 762
    _PUBLISHING._serialized_start = 765
    _PUBLISHING._serialized_end = 1189
    _JAVASETTINGS._serialized_start = 1192
    _JAVASETTINGS._serialized_end = 1419
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._serialized_start = 1363
    _JAVASETTINGS_SERVICECLASSNAMESENTRY._serialized_end = 1419
    _CPPSETTINGS._serialized_start = 1421
    _CPPSETTINGS._serialized_end = 1486
    _PHPSETTINGS._serialized_start = 1488
    _PHPSETTINGS._serialized_end = 1553
    _PYTHONSETTINGS._serialized_start = 1555
    _PYTHONSETTINGS._serialized_end = 1623
    _NODESETTINGS._serialized_start = 1625
    _NODESETTINGS._serialized_end = 1691
    _DOTNETSETTINGS._serialized_start = 1694
    _DOTNETSETTINGS._serialized_end = 2120
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._serialized_start = 2009
    _DOTNETSETTINGS_RENAMEDSERVICESENTRY._serialized_end = 2063
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._serialized_start = 2065
    _DOTNETSETTINGS_RENAMEDRESOURCESENTRY._serialized_end = 2120
    _RUBYSETTINGS._serialized_start = 2122
    _RUBYSETTINGS._serialized_end = 2188
    _GOSETTINGS._serialized_start = 2190
    _GOSETTINGS._serialized_end = 2254
    _METHODSETTINGS._serialized_start = 2257
    _METHODSETTINGS._serialized_end = 2592
    _METHODSETTINGS_LONGRUNNING._serialized_start = 2387
    _METHODSETTINGS_LONGRUNNING._serialized_end = 2592
# @@protoc_insertion_point(module_scope)
