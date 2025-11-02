from .structure import Structure
from ..repr_list import *
from ..datatypes import *


class Slot340(Structure):
    def __init__(self, data: bytearray):
        self.block_id = Short.decode(data)

        if (self.block_id != -1):
            self.item_count = Byte.decode(data)
            self.item_damage = Short.decode(data)

            if (data[0] == 0):
                self.nbt = data.pop(0)

            else:
                self.nbt = NBT.decode(data)