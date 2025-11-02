from ..packet import ServerPacket
from ....datatypes import *


class ServerJoinGamePacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = Integer.decode(data)
        self.gamemode = UnsignedByte.decode(data)
        self.dimension = Integer.decode(data)
        self.difficulty = UnsignedByte.decode(data)
        self.max_players = UnsignedByte.decode(data)
        self.level_type = String.decode(data)
        self.reduced_debug_info = Boolean.decode(data)