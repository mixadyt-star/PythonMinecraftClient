from ...packets import *

from abc import *


class PacketQueueManager(ABC):
    @abstractmethod
    def put_packet(self, packet: ServerPacket): ...

    @abstractmethod
    def get_packet(self) -> ServerPacket: ...

    @abstractmethod
    def has_packets(self) -> bool: ...