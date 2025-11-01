from .utils import *
from .datatype import DataType

class Boolean(DataType):
    def __init__(self, boolean: True):
        super().__init__(boolean)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(bool(multi_pop(data, 1)))

    def encode(self) -> bytes:
        return int(self.inp).to_bytes(1, "big")