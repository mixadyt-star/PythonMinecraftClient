from .datatype import DataType
from .varint import VarInt
from .utils import *

class String(DataType):
    def __init__(self, text: str):
        super().__init__(text)

    @classmethod
    def from_bytes(cls, data: bytearray):
        length = VarInt.from_bytes(data).inp
        
        return cls(multi_pop(data, length).decode())

    def encode(self) -> bytes:
        return VarInt(len(self.inp)).encode() + self.inp.encode()