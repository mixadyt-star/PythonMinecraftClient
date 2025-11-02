from ..packet import ServerPacket
from ....datatypes import *


class ServerEntityEquipmentPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.slot = VarInt.decode(data)
        self.item = ByteArray.decode(data)