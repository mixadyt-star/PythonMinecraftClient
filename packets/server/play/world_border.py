from ..packet import ServerPacket
from ....datatypes import *


class ServerWorldBorderPacket340(ServerPacket):
    def __init__(self, data, session):
        self.action = VarInt.decode(data)

        if (self.action == 0):
            self.diameter = Double.decode(data)

        elif (self.action == 1):
            self.old_diameter = Double.decode(data)
            self.new_diameter = Double.decode(data)
            self.speed = VarInt.decode(data)

        elif (self.action == 2):
            self.x = Double.decode(data)
            self.z = Double.decode(data)

        elif (self.action == 3):
            self.x = Double.decode(data)
            self.z = Double.decode(data)
            self.old_diameter = Double.decode(data)
            self.new_diameter = Double.decode(data)
            self.speed = VarInt.decode(data)
            self.portal_teleport_boundary = VarInt.decode(data)
            self.warning_time = VarInt.decode(data)
            self.warning_blocks = VarInt.decode(data)

        elif (self.action == 4):
            self.warning_time = VarInt.decode(data)

        elif (self.action == 5):
            self.warning_blocks = VarInt.decode(data)