from ..packet import ServerPacket
from ....datatypes import *


class ServerEntityHeadLookPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.head_yaw = UnsignedByte.decode(data)