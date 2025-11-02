from ..packet import ClientPacket
from ....datatypes import *


class ClientClientSettingsPacket340(ClientPacket):
    def __init__(self,
                 locale: str,
                 view_distance: int,
                 chat_mode: int,
                 chat_colors: bool,
                 displayed_skin_parts: int,
                 main_hand: int):
        
        super().__init__(0x04)

        self.locale = String.encode(locale)
        self.view_distance = Byte.encode(view_distance)
        self.chat_mode = VarInt.encode(chat_mode)
        self.chat_colors = Boolean.encode(chat_colors)
        self.displayed_skin_parts = UnsignedByte.encode(displayed_skin_parts)
        self.main_hand = VarInt.encode(main_hand)
