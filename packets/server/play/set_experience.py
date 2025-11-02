from ..packet import ServerPacket
from ....datatypes import *


class ServerSetExperiencePacket340(ServerPacket):
    def __init__(self, data, session):
        self.exp_bar = Float.decode(data)
        self.level = VarInt.decode(data)
        self.total_exp = VarInt.decode(data)