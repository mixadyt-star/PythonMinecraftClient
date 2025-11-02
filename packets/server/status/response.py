from ..packet import ServerPacket
from ....datatypes import *


class ServerStatusResponsePacket340(ServerPacket):
    def __init__(self, data, session):
        self.json_data = String.decode(data)