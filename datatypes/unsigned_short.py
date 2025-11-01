from .utils import *
from .datatype import DataType

class UnsignedShort(DataType):
    def __init__(self, num: int):
        super().__init__(num)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(int.from_bytes(multi_pop(data, 2)))

    def encode(self) -> bytes:
        return (self.inp & 0xFFFF).to_bytes(2, "big")