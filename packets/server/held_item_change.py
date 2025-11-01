from ..packet import Packet
from ...datatypes import *

class ServerHeldItemChangePacket340(Packet):
    def __init__(self,
                 slot: Byte):
        
        super().__init__(0x3a)

        self.slot = slot