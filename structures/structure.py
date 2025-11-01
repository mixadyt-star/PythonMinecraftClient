from ..datatypes import *

import inspect
from typing import Dict

class Structure:
    def __init__(self):
        pass

    @classmethod
    def from_bytes(cls, data: bytearray) -> bytes:
        kwargs: Dict[str, DataType] = {}

        for parameter in list(inspect.signature(cls.__init__).parameters.values())[1:]:
            if (type(parameter.annotation) == Optional):
                kwargs[parameter.name] = parameter.annotation.from_bytes(kwargs, data)
            else:
                kwargs[parameter.name] = parameter.annotation.from_bytes(data)

        return cls(**kwargs)

    def __repr__(self):
        repr = self.__class__.__name__ + ":\n"

        for name, var in self.__dict__.items():
            repr += "\t" + name + ": " + var.__repr__() + "\n"

        return repr