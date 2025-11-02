from ..packet import ServerPacket
from ....datatypes import *


class ServerEntityMetadataPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = VarInt.decode(data)
        self.metadata = ByteArray.decode(data)