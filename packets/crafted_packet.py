from ..datatypes import *

from typing import Dict

class CraftedPacket:
    def __init__(self, cls: object, kwargs: Dict[str, bytes]):
        self.cls = cls
        for name, value in kwargs.items():
            self.__setattr__(name, value)

    def pack(self) -> bytes:
        payload = bytes()

        for name, value in self.__dict__.items():
            if (name != "cls"):
                payload += value

        return VarInt(len(payload)).encode() + payload

    def __repr__(self):
        repr = "Crafted" + self.cls.__name__ + ":\n"

        for name, value in self.__dict__.items():
            if (name != "cls"):
                repr += "\t" + name + ": 0x" + value.hex() + "\n"

        return repr