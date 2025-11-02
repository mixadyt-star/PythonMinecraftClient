from .requirements import AdancementRequirements340
from .display import DisplayAdancement340
from ..structure import Structure
from ...repr_list import *
from ...datatypes import *


class Advancement340(Structure):
    def __init__(self, data: bytearray):
        self.identifier = String.decode(data)
        self.has_parent = Boolean.decode(data)

        if (self.has_parent):
            self.parent_id = String.decode(data)

        self.has_display = Boolean.decode(data)

        if (self.has_display):
            self.display = DisplayAdancement340(data)

        self.number_criteria = VarInt.decode(data)
        self.criterias = ReprList()

        for _ in range(self.number_criteria):
            self.criterias.append(String.decode(data))

        self.number_requirements = VarInt.decode(data)
        self.requirements = ReprList()

        for _ in range(self.number_requirements):
            self.requirements.append(AdancementRequirements340(data))