from ..packet import Packet
from ...datatypes import *

class ServerStatusResponsePacket340(Packet):
    def __init__(self,
                 json_data: String):
        
        super().__init__(0x00)
        
        self.json_data = json_data