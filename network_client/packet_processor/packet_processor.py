from ...packets import *

from abc import *


class PacketProcessor(ABC):
    @abstractmethod
    def process_packet(self, data: bytes, state: int) -> ServerPacket: ...