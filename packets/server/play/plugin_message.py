from ..packet import ServerPacket
from ....datatypes import *


class ServerPluginMessagePacket340(ServerPacket):
    def __init__(self, data, session):
        self.channel = String.decode(data)
        self.data = ByteArray.decode(data)