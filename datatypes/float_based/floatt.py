from ..datatype import DataType
from ..utils import *

import struct


class Float(DataType):
    @staticmethod
    def encode(data: float):
        return struct.pack('>f', data)
    
    @staticmethod
    def decode(data) -> float:
        return struct.unpack('>f', multi_pop(data, 4))[0]