from ..packet import Packet
from ...datatypes import *

class ClientHandshakePacket340(Packet):
    def __init__(self,
                 protocol_version: VarInt,
                 server_address: String,
                 server_port: UnsignedShort,
                 next_state: VarInt):
        
        super().__init__(0x00)

        self.protocol_version = protocol_version
        self.server_address = server_address
        self.server_port = server_port
        self.next_state = next_state
