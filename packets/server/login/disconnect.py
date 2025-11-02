from ..packet import ServerPacket
from ....datatypes import *


class ServerLoginDisconnectPacket340(ServerPacket):
    def __init__(self, data, session):
        self.reason = String.decode(data)