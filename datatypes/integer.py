from .utils import *
from .datatype import DataType

class Integer(DataType):
    def __init__(self, num: int):
        super().__init__(num)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(int.from_bytes(multi_pop(data, 4), signed=True))

    def encode(self) -> bytes:
        return (self.inp & 0xFFFFFFFF).to_bytes(4, "big")