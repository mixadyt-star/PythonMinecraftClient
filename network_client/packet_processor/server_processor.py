from .packet_processor import PacketProcessor
from ...packets import *


class ServerPacketProcessor(PacketProcessor):
    def __init__(self, server_factory: ServerPacketFactory):
        self.server_factory = server_factory

    def process_packet(self, data, state):
        return self.server_factory.create_packet(state, data)