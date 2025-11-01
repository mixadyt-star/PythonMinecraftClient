from ..datatypes import *
from .structure import Structure
from .player_list_item_property import PlayerListItemProperty

from typing import Dict

def check_display_name(fields: Dict[str, DataType]) -> bool:
    return fields["has_display_name"]

class PlayerListItemAddPlayer(Structure):
    def __init__(self,
                 properties: PrefixedArray[PlayerListItemProperty],
                 gamemode: VarInt,
                 ping: VarInt,
                 has_display_name: Boolean,
                 display_name: Optional[String, check_display_name]):
        
        self.properties = properties
        self.gamemode = gamemode
        self.ping = ping
        self.has_display_name = has_display_name
        if (display_name is not None):
            self.display_name = display_name