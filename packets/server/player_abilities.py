from ..packet import Packet
from ...datatypes import *

class ServerPlayerAbilitiesPacket340(Packet):
    def __init__(self,
                 flags: Byte,
                 flying_speed: Float,
                 field_of_view: Float):
        
        super().__init__(0x2c)

        self.flags = flags
        self.flying_speed = flying_speed
        self.field_of_view = field_of_view