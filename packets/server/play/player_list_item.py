from ..packet import ServerPacket
from ....structures import *
from ....repr_list import *
from ....datatypes import *


class ServerPlayerListItemPacket340(ServerPacket):
    def __init__(self, data, session):
        self.action = VarInt.decode(data)
        self.number_of_players = VarInt.decode(data)
        self.players = ReprList()

        for _ in range(self.number_of_players):
            self.players.append(PlayerListItem340(data, self.action))
            