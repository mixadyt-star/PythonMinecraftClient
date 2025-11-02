from ..structure import Structure
from ..slot import Slot340
from ...repr_list import *
from ...datatypes import *


class DisplayAdancement340(Structure):
    def __init__(self, data: bytearray):
        self.title = String.decode(data)
        self.description = String.decode(data)
        self.icon = Slot340(data)
        self.frame_type = VarInt.decode(data)
        self.flags = Integer.decode(data)

        if (self.flags & 0x01):
            self.backgound_texture = String.decode(data)

        self.x = Float.decode(data)
        self.y = Float.decode(data)