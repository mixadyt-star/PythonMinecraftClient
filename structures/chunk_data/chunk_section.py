from ..structure import Structure
from ...dataclass import Session
from ...repr_list import *
from ...datatypes import *


class ChunkSection340(Structure):
    def __init__(self, data: bytearray, session: Session):
        self.bits_per_block = UnsignedByte.decode(data)
        self.palette_length = VarInt.decode(data)
        self.palette = ReprList()

        for _ in range(self.palette_length):
            self.palette.append(VarInt.decode(data))

        self.data_length = VarInt.decode(data)
        self.data = ReprList(repr=False)

        for _ in range(self.data_length):
            self.data.append(Long.decode(data))

        self.blocks_light = ReprList(repr=False)

        for _ in range(2048):
            self.blocks_light.append(Byte.decode(data))

        if (session.dimension == "Overworld"):
            self.sky_light = ReprList(repr=False)

            for _ in range(2048):
                self.sky_light.append(Byte.decode(data))