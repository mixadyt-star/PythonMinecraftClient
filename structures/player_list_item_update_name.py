from ..datatypes import *
from .structure import Structure

from typing import Dict

def check_display_name(fields: Dict[str, DataType]) -> bool:
    return fields["has_display_name"]

class PlayerListItemUpdateDisplayName(Structure):
    def __init__(self,
                 has_display_name: Boolean,
                 display_name: Optional[String, check_display_name]):
        
        self.has_display_name = has_display_name
        if (display_name is not None):
            self.display_name = display_name