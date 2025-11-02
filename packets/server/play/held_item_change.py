from ..packet import ServerPacket
from ....datatypes import *


class ServerHeldItemChangePacket340(ServerPacket):
    def __init__(self, data, session):
        self.slot = Byte.decode(data)