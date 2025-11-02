from ..structure import Structure
from ...datatypes import *


class EntityModifier340(Structure):
    def __init__(self, data: bytearray):
        self.uuid = UUID.decode(data)
        self.amount = Double.decode(data)
        self.operation = Byte.decode(data)