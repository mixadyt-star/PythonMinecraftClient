from .utils import *
from .datatype import DataType

class Long(DataType):
    def __init__(self, num: int):
        super().__init__(num)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(int.from_bytes(multi_pop(data, 8), signed=True))

    def encode(self) -> bytes:
        return (self.inp & 0xFFFFFFFFFFFFFFFF).to_bytes(8, "big")