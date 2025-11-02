from ..packet import ServerPacket
from ....datatypes import *


class ServerTimeUpdatePacket340(ServerPacket):
    def __init__(self, data, session):
        self.world_age = Long.decode(data)
        self.time_of_day = Long.decode(data)