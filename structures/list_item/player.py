from .property import PropertyListItem340
from ..structure import Structure
from ...repr_list import *
from ...datatypes import *


class PlayerListItem340(Structure):
    def __init__(self, data: bytearray, action: int):
        self.uuid = UUID.decode(data)

        if (action == 0):
            self.name = String.decode(data)
            self.number_of_properties = VarInt.decode(data)
            self.properties = ReprList()

            for _ in range(self.number_of_properties):
                self.properties.append(PropertyListItem340(data))

            self.gamemode = VarInt.decode(data)
            self.ping = VarInt.decode(data)
            self.has_display_name = Boolean.decode(data)

            if (self.has_display_name):
                self.display_name = String.decode(data)
        
        elif (action == 1):
            self.gamemode = VarInt.decode(data)

        elif (action == 2):
            self.ping = VarInt.decode(data)

        elif (action == 3):
            self.has_display_name = Boolean.decode(data)

            if (self.has_display_name):
                self.display_name = String.decode(data)

        elif (action == 4):
            pass