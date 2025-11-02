from ..datatype import DataType
from ..utils import *


class Long(DataType):
    @staticmethod
    def encode(data: int):
        return (data & 0xFFFFFFFFFFFFFFFF).to_bytes(8, "big")
    
    @staticmethod
    def decode(data) -> int:
        return int.from_bytes(multi_pop(data, 8), signed=True)