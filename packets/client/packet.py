from ...datatypes import *


class ClientPacket:
    def __init__(self, packet_id: int):
        self.packet_id = VarInt.encode(packet_id)

    def pack(self) -> bytes:
        payload = bytes()

        for value in self.__dict__.values():
            payload += value

        return VarInt.encode(len(payload)) + payload

    def __repr__(self, depth: int = 0) -> str:
        repr = self.__class__.__name__ + ":\n"

        for name, var in self.__dict__.items():
            try:
                repr += "\t" + "\t" * depth + name + ": " + var.__repr__(depth=depth + 1) + "\n"
            except TypeError:
                repr += "\t" + "\t" * depth + name + ": " + var.__repr__() + "\n"

        return repr