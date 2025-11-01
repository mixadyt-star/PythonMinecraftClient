from ..packet import Packet
from ...datatypes import *

class ClientLoginStartPacket340(Packet):
    def __init__(self,
                 name: String):
        
        super().__init__(0x00)

        self.name = name
