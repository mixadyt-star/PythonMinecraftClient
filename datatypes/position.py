from .datatype import DataType
from .int_based import *
from .utils import *

from typing import *


class Position(DataType):
    @staticmethod
    def encode(data: Tuple[int, int, int]):
        x, y, z = data
        return Long.encode(((x & 0x3FFFFFF) << 38) | ((y & 0xFFF) << 26) | (z & 0x3FFFFFF))
    
    @staticmethod
    def decode(data) -> Tuple[int, int, int]:
        val = Long.decode(data)
        x = val >> 38
        y = (val >> 26) & 0xFFF
        z = val & 0X3FFFFFF

        if (x >= 0x2000000): x -= 0x4000000
        if (y >= 0x0000800): y -= 0x0001000
        if (z >= 0x2000000): z -= 0x4000000

        return x, y, z