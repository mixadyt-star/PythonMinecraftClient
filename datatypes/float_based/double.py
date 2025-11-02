from ..datatype import DataType
from ..utils import *

import struct


class Double(DataType):
    @staticmethod
    def encode(data: float):
        return struct.pack('>d', data)
    
    @staticmethod
    def decode(data) -> float:
        return struct.unpack('>d', multi_pop(data, 8))[0]