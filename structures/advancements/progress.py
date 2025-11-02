from .criterion_progress import CriterionProgress340
from ..structure import Structure
from ...repr_list import *
from ...datatypes import *


class AdvancementProgress340(Structure):
    def __init__(self, data: bytearray):
        self.identifier = String.decode(data)
        self.size = VarInt.decode(data)
        self.criterias = ReprList()

        for _ in range(self.size):
            self.criterias.append(CriterionProgress340(data))