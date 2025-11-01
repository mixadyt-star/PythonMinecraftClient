from ..packet import Packet
from ...datatypes import *

class ServerPluginMessagePacket340(Packet):
    def __init__(self,
                 channel: String,
                 data: ByteArray):
        
        super().__init__(0x18)

        self.channel = channel
        self.data = data