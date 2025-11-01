from ..packet import Packet
from ...datatypes import *

class ClientStatusRequestPacket340(Packet):
    def __init__(self):
        
        super().__init__(0x00)
