from enum import Enum


class State(Enum):
    HANDSHAKE = 0x00
    STATUS    = 0x01
    LOGIN     = 0x02
    PLAY      = 0x03