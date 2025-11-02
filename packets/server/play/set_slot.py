from ..packet import ServerPacket
from ....structures import *
from ....datatypes import *


class ServerSetSlotPacket340(ServerPacket):
    def __init__(self, data, session):
        self.window_id = Byte.decode(data)
        self.slot = Short.decode(data)
        self.slot_data = Slot340(data)