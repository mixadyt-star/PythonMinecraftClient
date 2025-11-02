from ..datatype import DataType
from ..utils import *


class Boolean(DataType):
    @staticmethod
    def encode(data: bool):
        return int(data).to_bytes(1, "big")
    
    @staticmethod
    def decode(data) -> bool:
        return bool(data.pop(0))