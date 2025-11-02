from ..packet import ClientPacket
from ....datatypes import *


class ClientLoginStartPacket340(ClientPacket):
    def __init__(self,
                 name: str):
        
        super().__init__(0x00)

        self.name = String.encode(name)
