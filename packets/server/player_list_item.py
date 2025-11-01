from ..packet import Packet
from ...datatypes import *

from typing import Tuple

class Player(DataType):
    def __init__(self,
                 inp: Tuple[String, PrefixedArray, VarInt, VarInt, ]):
        super().__init__(inp)

class ServerPlayerListItemPacket340(Packet):
    def __init__(self,
                 action: VarInt,
                 num_of_players: VarInt):
        
        super().__init__(0x2e)

        self.action = action
        self.num_of_players = num_of_players