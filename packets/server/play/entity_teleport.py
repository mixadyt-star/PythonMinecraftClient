from ..packet import ServerPacket
from ....datatypes import *


class ServerEntityTeleportPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.x = Double.decode(data)
        self.y = Double.decode(data)
        self.z = Double.decode(data)
        self.yaw = UnsignedByte.decode(data)
        self.pitch = UnsignedByte.decode(data)
        self.on_ground = Boolean.decode(data)