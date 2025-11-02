from ..packet import ServerPacket
from ....datatypes import *


class ServerChangeGameStatePacket340(ServerPacket):
    def __init__(self, data, session):
        self.reason = UnsignedByte.decode(data)
        self.value = Float.decode(data)