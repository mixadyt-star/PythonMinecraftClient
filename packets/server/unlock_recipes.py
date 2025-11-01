from ..packet import Packet
from ...datatypes import *

from typing import Dict

def check_list2(fields: Dict[str, DataType]) -> bool:
    return fields["action"].inp == 0

class ServerUnlockRecipesPacket340(Packet):
    def __init__(self,
                 action: VarInt,
                 book_open: Boolean,
                 filtering_craftable: Boolean,
                 list1: PrefixedArray[VarInt],
                 list2: Optional[PrefixedArray[VarInt], check_list2]):
        
        super().__init__(0x31)
        
        self.action = action
        self.book_open = book_open
        self.filtering_craftable = filtering_craftable
        self.list1 = list1
        if (list2 is not None):
            self.list2 = list2