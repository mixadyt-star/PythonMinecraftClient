from ..packet import ServerPacket
from ....datatypes import *


class ServerUpdateHealthPacket340(ServerPacket):
    def __init__(self, data, session):
        self.health = Float.decode(data)
        self.food = VarInt.decode(data)
        self.food_saturation = Float.decode(data)