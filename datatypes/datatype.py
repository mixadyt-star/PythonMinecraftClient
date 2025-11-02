from typing import *
from abc import *


class DataType(ABC):
    @staticmethod
    @abstractmethod
    def encode(data: Any) -> bytes: ...

    @staticmethod
    @abstractmethod
    def decode(data: bytearray) -> Any: ...