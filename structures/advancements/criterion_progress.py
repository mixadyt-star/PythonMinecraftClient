from ..structure import Structure
from ...repr_list import *
from ...datatypes import *


class CriterionProgress340(Structure):
    def __init__(self, data: bytearray):
        self.identifier = String.decode(data)
        self.achieved = Boolean.decode(data)

        if (self.achieved):
            self.achieving_date = Long.decode(data)