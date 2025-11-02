from ..structure import Structure
from ...datatypes import *


class PropertyListItem340(Structure):
    def __init__(self, data: bytearray):
        self.name = String.decode(data)
        self.value = String.decode(data)
        self.is_signed = Boolean.decode(data)

        if (self.is_signed):
            self.signature = String.decode(data)