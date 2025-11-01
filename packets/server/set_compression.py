from ..packet import Packet
from ...datatypes import *

class ServerSetCompressionPacket340(Packet):
    def __init__(self,
                 threshold: VarInt):
        
        super().__init__(0x03)

        self.threshold = threshold