from ..packet import Packet
from ...datatypes import *

class ServerServerDifficultyPacket340(Packet):
    def __init__(self,
                 difficulty: UnsignedByte):
        
        super().__init__(0x0d)

        self.difficulty = difficulty