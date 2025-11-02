from ..packet import ServerPacket
from ....datatypes import *


class ServerSpawnPositionPacket340(ServerPacket):
    def __init__(self, data, session):
        self.location = Position.decode(data)