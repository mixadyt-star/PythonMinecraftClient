from ..datatype import DataType
from ..utils import *


class UnsignedShort(DataType):
    @staticmethod
    def encode(data: int):
        return (data & 0xFFFF).to_bytes(2, "big")
    
    @staticmethod
    def decode(data) -> int:
        return int.from_bytes(multi_pop(data, 2))