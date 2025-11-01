from ..packet import Packet
from ...datatypes import *

class ServerStatusPongPacket340(Packet):
    def __init__(self,
                 payload: Long):
        
        super().__init__(0x01)

        self.payload = payload