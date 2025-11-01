from .utils import *
from .datatype import DataType
from .varint import VarInt

from typing import List

class PrefixedArray(DataType):
    def __init__(self, item_class: DataType):
        self.item_class = item_class

    def __class_getitem__(cls, datatype: DataType):
        return cls(datatype)

    def __call__(self, array: List[DataType]):
        super().__init__(array)

        return self

    def from_bytes(self, data: bytearray):
        return PrefixedArray[self.item_class]([self.item_class.from_bytes(data) for i in range(VarInt.from_bytes(data).inp)])

    def encode(self) -> bytes:
        return VarInt(len(self.inp)).encode() + b''.join([x.encode() for x in self.inp])