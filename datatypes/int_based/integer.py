from ..datatype import DataType
from ..utils import *


class Integer(DataType):
    @staticmethod
    def encode(data: int):
        return (data & 0xFFFFFFFF).to_bytes(4, "big")
    
    @staticmethod
    def decode(data) -> int:
        return int.from_bytes(multi_pop(data, 4), signed=True)