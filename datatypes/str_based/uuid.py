from ..datatype import DataType
from ..utils import *

import uuid


class UUID(DataType):
    @staticmethod
    def encode(data: str):
        return uuid.UUID(data).bytes
    
    @staticmethod
    def decode(data) -> str:
        return str(uuid.UUID(bytes=multi_pop(data, 16)))