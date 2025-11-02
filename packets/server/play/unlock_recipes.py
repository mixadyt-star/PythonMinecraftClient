from ..packet import ServerPacket
from ....repr_list import *
from ....datatypes import *


class ServerUnlockRecipesPacket340(ServerPacket):
    def __init__(self, data, session):
        self.action = VarInt.decode(data)
        self.book_open = Boolean.decode(data)
        self.filtering_craftable = Boolean.decode(data)
        self.array_size1 = VarInt.decode(data)
        self.list1 = ReprList()
        
        for _ in range(self.array_size1):
            self.list1.append(VarInt.decode(data))

        if (self.action == 0):
            self.array_size2 = VarInt.decode(data)
            self.list2 = ReprList()
            
            for _ in range(self.array_size2):
                self.list2.append(VarInt.decode(data))