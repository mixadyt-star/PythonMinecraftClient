from ..packet import Packet
from ...datatypes import *

class ClientClientSettingsPacket340(Packet):
    def __init__(self,
                 locale: String,
                 view_distance: Byte,
                 chat_mode: VarInt,
                 chat_colors: Boolean,
                 displayed_skin_parts: UnsignedByte,
                 main_hand: VarInt):
        
        super().__init__(0x04)

        self.locale = locale
        self.view_distance = view_distance
        self.chat_mode = chat_mode
        self.chat_colors = chat_colors
        self.displayed_skin_parts = displayed_skin_parts
        self.main_hand = main_hand
