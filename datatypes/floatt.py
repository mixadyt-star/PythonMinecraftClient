from .utils import *
from .datatype import DataType

import struct

class Float(DataType):
    def __init__(self, num: float):
        super().__init__(num)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(struct.unpack('>f', multi_pop(data, 4))[0])

    def encode(self) -> bytes:
        return struct.pack('>f', self.inp)