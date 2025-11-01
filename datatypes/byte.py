from .utils import *
from .datatype import DataType

class Byte(DataType):
    def __init__(self, num: int):
        super().__init__(num)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(int.from_bytes(multi_pop(data, 1), signed=True))

    def encode(self) -> bytes:
        return (self.inp & 0xFF).to_bytes(1, "big")