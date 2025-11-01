from ..datatypes import *
from .structure import Structure

from typing import Dict

def check_signature(fields: Dict[str, DataType]) -> bool:
    return fields["signed"]

class PlayerListItemProperty(Structure):
    def __init__(self,
                 name: String,
                 value: String,
                 signed: Boolean,
                 signature: Optional[String, check_signature]):
        
        self.name = name
        self.value = value
        self.signed = signed
        if (signature is not None):
            self.signature = signature