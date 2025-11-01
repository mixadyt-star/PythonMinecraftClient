from ..packet import Packet
from ...datatypes import *

class ServerJoinGamePacket340(Packet):
    def __init__(self,
                 eid: Integer,
                 gamemode: UnsignedByte,
                 dimension: Integer,
                 difficulty: UnsignedByte,
                 max_players: UnsignedByte,
                 level_type: String,
                 reduced_debug_info: Boolean):
        
        super().__init__(0x23)

        self.eid = eid
        self.gamemode = gamemode
        self.dimension = dimension
        self.difficulty = difficulty
        self.max_players = max_players
        self.level_type = level_type
        self.reduced_debug_info = reduced_debug_info