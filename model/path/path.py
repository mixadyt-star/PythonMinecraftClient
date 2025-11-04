from typing import *
from abc import *


class Path(ABC):
    @abstractmethod
    def join(key: Any) -> 'Path': ...

    @abstractmethod
    def apply(self, traversal: Any): ...