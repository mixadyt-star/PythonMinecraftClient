from ..packet import Packet
from ...datatypes import *

class ServerEntityStatusPacket340(Packet):
    def __init__(self,
                 eid: Integer,
                 status: Byte):
        
        super().__init__(0x1b)

        self.eid = eid
        self.status = status