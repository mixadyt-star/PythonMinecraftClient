from ..datatype import DataType
from ..int_based import *
from ..utils import *


class String(DataType):
    @staticmethod
    def encode(data: str):
        return VarInt.encode(len(data)) + data.encode()
    
    @staticmethod
    def decode(data) -> str:
        length = VarInt.decode(data)
        
        return multi_pop(data, length).decode()