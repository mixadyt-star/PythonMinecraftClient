from .utils import *
from .datatype import DataType

from typing import Dict, Tuple, Callable

class Optional(DataType):
    def __init__(self, child: DataType):
        super().__init__(child)

    def __class_getitem__(cls, datatype: DataType):
        return cls(datatype)

    def from_bytes(self, fields: Dict[str, DataType], data: bytearray):
        if (self.check_callback(fields)):
            return Optional[self.inp.from_bytes(data)]
        
        return None

    def encode(self) -> bytes:
        return self.inp.encode()