from ..packet import ServerPacket
from ....datatypes import *


class ServerSpawnMobPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.euuid = UUID.decode(data)
        self.type = VarInt.decode(data)
        self.x = Double.decode(data)
        self.y = Double.decode(data)
        self.z = Double.decode(data)
        self.yaw = UnsignedByte.decode(data)
        self.pitch = UnsignedByte.decode(data)
        self.head_pitch = UnsignedByte.decode(data)
        self.vel_x = Short.decode(data)
        self.vel_y = Short.decode(data)
        self.vel_z = Short.decode(data)
        self.metadata = ByteArray.decode(data)