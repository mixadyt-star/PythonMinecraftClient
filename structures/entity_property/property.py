from ...repr_list import ReprList
from .modifier import EntityModifier340
from ..structure import Structure
from ...datatypes import *


class EntityProperty340(Structure):
    def __init__(self, data: bytearray):
        self.key = String.decode(data)
        self.value = Double.decode(data)
        self.number_modifiers = VarInt.decode(data)
        self.modifiers = ReprList()

        for _ in range(self.number_modifiers):
            self.modifiers.append(EntityModifier340(data))