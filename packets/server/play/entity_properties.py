from ....repr_list import ReprList
from ..packet import ServerPacket
from ....structures import *
from ....datatypes import *


class ServerEntityPropertiesPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.number_properties = Integer.decode(data)
        self.properties = ReprList()

        for _ in range(self.number_properties):
            self.properties.append(EntityProperty340(data))