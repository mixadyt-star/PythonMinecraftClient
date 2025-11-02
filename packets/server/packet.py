from ...session import Session
from ...datatypes import *

from abc import *

class ServerPacket(ABC):
    @abstractmethod
    def __init__(self, data: bytearray, session: Session): ...

    def __repr__(self, depth: int = 0) -> str:
        repr = self.__class__.__name__ + ":\n"

        for name, var in self.__dict__.items():
            try:
                repr += "\t" + "\t" * depth + name + ": " + var.__repr__(depth=depth + 1) + "\n"
            except TypeError:
                repr += "\t" + "\t" * depth + name + ": " + var.__repr__() + "\n"

        return repr