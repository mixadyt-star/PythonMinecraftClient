from ..packet import ClientPacket
from ....datatypes import *


class ClientStatusPingPacket340(ClientPacket):
    def __init__(self,
                 payload: int):
        
        super().__init__(0x01)

        self.payload = Long.encode(payload)
