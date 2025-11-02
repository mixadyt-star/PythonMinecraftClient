from ..packet import ServerPacket
from ....datatypes import *


class ServerEntityStatusPacket340(ServerPacket):
    def __init__(self, data, session):
        self.eid = Integer.decode(data)
        self.status = Byte.decode(data)