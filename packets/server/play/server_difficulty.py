from ..packet import ServerPacket
from ....datatypes import *


class ServerServerDifficultyPacket340(ServerPacket):
    def __init__(self, data, session):
        self.difficulty = UnsignedByte.decode(data)