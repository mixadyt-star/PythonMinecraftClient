from ...dataclass import *
from ...model import *

from typing import *
from abc import *


class PacketFactory(ABC):
    @abstractmethod
    def create_packet(self, craft_data: CraftData) -> Model: ...