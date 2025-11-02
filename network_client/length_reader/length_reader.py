from ..connection import *

from abc import *


class LengthReader(ABC):
    @staticmethod
    @abstractmethod
    def read_length(connection: Connection) -> int: ...