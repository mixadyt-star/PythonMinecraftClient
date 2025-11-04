from typing import *
from abc import *


class Context(ABC):
    @abstractmethod
    def append(self, key: Any, value: Any): ...

    @abstractmethod
    def get(self, key: Any) -> Any: ...