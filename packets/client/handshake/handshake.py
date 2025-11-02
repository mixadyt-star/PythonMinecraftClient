from ..packet import ClientPacket
from ....datatypes import *


class ClientHandshakePacket340(ClientPacket):
    def __init__(self,
                 protocol_version: int,
                 server_address: str,
                 server_port: int,
                 next_state: int):
        
        super().__init__(0x00)

        self.protocol_version = VarInt.encode(protocol_version)
        self.server_address = String.encode(server_address)
        self.server_port = UnsignedShort.encode(server_port)
        self.next_state = VarInt.encode(next_state)
