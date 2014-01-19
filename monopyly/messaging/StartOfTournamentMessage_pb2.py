# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='StartOfTournamentMessage.proto',
  package='Messaging',
  serialized_pb=b'\n\x1eStartOfTournamentMessage.proto\x12\tMessaging\"\x9a\x01\n\x18StartOfTournamentMessage\x12\x44\n\x0cplayer_infos\x18\x01 \x03(\x0b\x32..Messaging.StartOfTournamentMessage.PlayerInfo\x1a\x38\n\nPlayerInfo\x12\x15\n\rplayer_number\x18\x01 \x01(\x05\x12\x13\n\x0bplayer_name\x18\x02 \x01(\t')




_STARTOFTOURNAMENTMESSAGE_PLAYERINFO = descriptor.Descriptor(
  name='PlayerInfo',
  full_name='Messaging.StartOfTournamentMessage.PlayerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='player_number', full_name='Messaging.StartOfTournamentMessage.PlayerInfo.player_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='player_name', full_name='Messaging.StartOfTournamentMessage.PlayerInfo.player_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode("utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=144,
  serialized_end=200,
)

_STARTOFTOURNAMENTMESSAGE = descriptor.Descriptor(
  name='StartOfTournamentMessage',
  full_name='Messaging.StartOfTournamentMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='player_infos', full_name='Messaging.StartOfTournamentMessage.player_infos', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_STARTOFTOURNAMENTMESSAGE_PLAYERINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=46,
  serialized_end=200,
)

_STARTOFTOURNAMENTMESSAGE_PLAYERINFO.containing_type = _STARTOFTOURNAMENTMESSAGE;
_STARTOFTOURNAMENTMESSAGE.fields_by_name['player_infos'].message_type = _STARTOFTOURNAMENTMESSAGE_PLAYERINFO
DESCRIPTOR.message_types_by_name['StartOfTournamentMessage'] = _STARTOFTOURNAMENTMESSAGE

StartOfTournamentMessage = reflection.GeneratedProtocolMessageType('StartOfTournamentMessage', (message.Message,),
    {
      'DESCRIPTOR': _STARTOFTOURNAMENTMESSAGE,
      'PlayerInfo': reflection.GeneratedProtocolMessageType('PlayerInfo', (message.Message,),
          {
            'DESCRIPTOR': _STARTOFTOURNAMENTMESSAGE_PLAYERINFO,
            # @@protoc_insertion_point(class_scope:Messaging.StartOfTournamentMessage.PlayerInfo)
          }),
      # @@protoc_insertion_point(class_scope:Messaging.StartOfTournamentMessage)
    })

# @@protoc_insertion_point(module_scope)
