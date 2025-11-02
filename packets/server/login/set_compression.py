from ..packet import ServerPacket
from ....datatypes import *


class ServerSetCompressionPacket340(ServerPacket):
    def __init__(self, data, session):
        self.threshold = VarInt.decode(data)