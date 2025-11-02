from ..packet import ServerPacket
from ....datatypes import *


class ServerEntityVelocityPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.vel_x = Short.decode(data)
        self.vel_y = Short.decode(data)
        self.vel_z = Short.decode(data)