from ..packet import ServerPacket
from ....datatypes import *


class ServerEntityRelativeMovePacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.delta_x = Short.decode(data)
        self.delta_y = Short.decode(data)
        self.delta_z = Short.decode(data)
        self.on_ground = Boolean.decode(data)