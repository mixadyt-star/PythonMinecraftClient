from ..packet import Packet
from ...datatypes import *

class ServerLoginDisconnectPacket340(Packet):
    def __init__(self,
                 reason: String):
        
        super().__init__(0x00)

        self.reason = reason