from ..datatype import DataType
from ..utils import *


class ByteArray(DataType):
    @staticmethod
    def encode(data: bytearray):
        return bytes(data)
    
    @staticmethod
    def decode(data) -> bytearray:
        return data