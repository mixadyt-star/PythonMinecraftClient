from .session import Session

from dataclasses import *


@dataclass
class CraftData:
    packet_data: bytearray
    session: Session