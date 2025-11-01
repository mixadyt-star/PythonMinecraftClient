from .utils import *
from .datatype import DataType

import uuid

class UUID(DataType):
    def __init__(self, uuid: str):
        super().__init__(uuid)

    @classmethod
    def from_bytes(cls, data: bytearray):
        return cls(str(uuid.UUID(bytes=multi_pop(data, 16))))

    def encode(self) -> bytes:
        return uuid.UUID(self.inp).bytes