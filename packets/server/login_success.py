from ..packet import Packet
from ...datatypes import *

class ServerLoginSuccessPacket340(Packet):
    def __init__(self,
                 uuid: String,
                 name: String):
        
        super().__init__(0x02)

        self.uuid = uuid
        self.name = name