from ..packet import ServerPacket
from ....datatypes import *


class ServerPositionAndViewPacket340(ServerPacket):
    def __init__(self, data, session):
        self.x = Double.decode(data)
        self.y = Double.decode(data)
        self.z = Double.decode(data)
        self.yaw = Float.decode(data)
        self.pitch = Float.decode(data)
        self.flags = Byte.decode(data)
        self.teleport_id = VarInt.decode(data)