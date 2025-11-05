from ..datatypes import *
from ..dataclass import *
from .context import *

from typing import *


class Validator:
    datatype: DataType
    _condition: Callable[[Context, CraftData], bool]

def validator(datatype: DataType,
              condition: Callable[[Context, CraftData], bool]):
    
    validator = Validator
    validator.datatype = datatype
    validator._condition = condition

    return Validator