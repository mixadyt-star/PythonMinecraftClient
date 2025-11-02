from ..packet import ServerPacket
from ....datatypes import *


class ServerPlayerAbilitiesPacket340(ServerPacket):
    def __init__(self, data, session):
        self.flags = Byte.decode(data)
        self.flying_speed = Float.decode(data)
        self.field_of_view = Float.decode(data)