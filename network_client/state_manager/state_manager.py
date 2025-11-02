from abc import *


class StateManager(ABC):
    @property
    @abstractmethod
    def state(self) -> int: ...

    @state.setter
    @abstractmethod
    def state(self, state: int): ...