from ..datatype import DataType
from ..utils import *


class UnsignedByte(DataType):
    @staticmethod
    def encode(data: int):
        return (data & 0xFF).to_bytes(1, "big")
    
    @staticmethod
    def decode(data) -> int:
        return int.from_bytes(multi_pop(data, 1))