from ..structure import Structure
from ...repr_list import *
from ...datatypes import *


class AdancementRequirements340(Structure):
    def __init__(self, data: bytearray):
        self.length = VarInt.decode(data)
        self.requirements = ReprList()

        for _ in range(self.length):
            self.requirements.append(String.decode(data))