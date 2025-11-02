from ....repr_list import ReprList
from ..packet import ServerPacket
from ....structures import *
from ....datatypes import *


class ServerAdvancementsPacket340(ServerPacket):
    def __init__(self, data, session):
        self.reset = Boolean.decode(data)
        self.advancements_size = VarInt.decode(data)
        self.advancements = ReprList()

        for _ in range(self.advancements_size):
            self.advancements.append(Advancement340(data))

        self.identifiers_size = VarInt.decode(data)
        self.identifiers = ReprList()

        for _ in range(self.identifiers_size):
            self.identifiers.append(String.decode(data))

        self.progress_size = VarInt.decode(data)
        self.progresses = ReprList()

        for _ in range(self.progress_size):
            self.progresses.append(AdvancementProgress340(data))