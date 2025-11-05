from dataclasses import *
from ..enums import *


@dataclass
class Session:
    state: State   = State.HANDSHAKE
    dimension: str = "Overworld"