from ..packet import ServerPacket
from ....datatypes import *


class ServerStatusPongPacket340(ServerPacket):
    def __init__(self, data, session):
        self.payload = Long.decode(data)