from ..packet import ServerPacket
from ....datatypes import *


class ServerKeepAlivePacket340(ServerPacket):
    def __init__(self, data, session):
        self.id = Long.decode(data)