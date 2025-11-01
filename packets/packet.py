from ..datatypes import *
from .crafted_packet import CraftedPacket

class Packet:
    def __init__(self, packet_id: int):
        self.packet_id = VarInt(packet_id)

    def craft(self) -> CraftedPacket:
        return CraftedPacket(self.__class__, {name: var.encode() for name, var in self.__dict__.items()})

    def __repr__(self):
        repr = self.__class__.__name__ + ":\n"

        for name, var in self.__dict__.items():
            repr += "\t" + name + ": " + var.__repr__() + "\n"

        return repr