from ..packet import ServerPacket
from ....datatypes import *


class ServerLoginSuccessPacket340(ServerPacket):
    def __init__(self, data, session):
        self.uuid = String.decode(data)
        self.name = String.decode(data)