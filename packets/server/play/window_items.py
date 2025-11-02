from ..packet import ServerPacket
from ....datatypes import *


class ServerWindowItemsPacket340(ServerPacket):
    def __init__(self, data, session):
        self.window_id = UnsignedByte.decode(data)
        self.count = Short.decode(data)
        self.slot_data = ByteArray.decode(data)