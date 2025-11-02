from abc import *


class Connection(ABC):
    @abstractmethod
    def connect(self, address: str, port: int): ...

    @abstractmethod
    def send(self, data: bytes): ...

    @abstractmethod
    def recv(self, length: int) -> bytes: ...

    @abstractmethod
    def close(self): ...

    @property
    @abstractmethod
    def connected(self) -> bool: ...