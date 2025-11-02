from ..packet import ClientPacket
from ....datatypes import *


class ClientStatusRequestPacket340(ClientPacket):
    def __init__(self):
        
        super().__init__(0x00)
