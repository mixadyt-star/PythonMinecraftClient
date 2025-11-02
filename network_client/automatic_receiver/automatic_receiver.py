from abc import *


class AutomaticPacketReceiver(ABC):
    @abstractmethod
    def start(self): ...

    @abstractmethod
    def stop(self): ...