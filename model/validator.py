from ..datatypes import *
from .context import *

from typing import *


class Validator:
    datatype: DataType
    _condition: Callable[[Context, bytearray], bool]

def validator(datatype: DataType,
              condition: Callable[[Context, bytearray], bool]):
    
    validator = Validator
    validator.datatype = datatype
    validator._condition = condition

    return Validator