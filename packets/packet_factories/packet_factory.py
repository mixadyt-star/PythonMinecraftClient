from ...session import Session
from ...datatypes import *
from ..server import *

from typing import *


class ServerPacketFactory:
    def __init__(self, session: Session):
        self.packets: Dict[int, Dict[int, Type[ServerPacket]]] = {}
        self.session = session

    def register(self, id: integer, state: integer, packet: Type[ServerPacket]):
        self.packets[state] = self.packets.get(state, {})
        self.packets[state][id] = packet

    def create_packet(self, state: integer, data: bytes) -> ServerPacket:
        data = bytearray(data)
        id = VarInt.decode(data)

        try:
            return self.packets[state][id](data, self.session)
        except KeyError:
            return "Ignored"