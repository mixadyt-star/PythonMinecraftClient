from .packet_factory import PacketFactory
from ...datatypes import *
from .protocol import *


class ServerPacketFactory(PacketFactory):
    def __init__(self, protocol: Protocol):
        self.protocol = protocol

    def create_packet(self, craft_data):
        id = VarInt.decode(craft_data.packet_data)
        model = self.protocol.get_model(
            state=craft_data.session.state,
            id=id,
        )

        return model(craft_data)