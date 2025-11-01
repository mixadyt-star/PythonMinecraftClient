from .utils import *
from .datatype import DataType

class ByteArray(DataType):
    def __init__(self, array: bytes):
        super().__init__(array)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(bytes(data))

    def encode(self) -> bytes:
        return self.inp