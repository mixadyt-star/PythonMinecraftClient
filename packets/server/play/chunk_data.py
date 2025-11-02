from ....repr_list import ReprList
from ..packet import ServerPacket
from ....structures import *
from ....datatypes import *


class ServerChunkDataPacket340(ServerPacket):
    def __init__(self, data, session):
        self.chunk_x = Integer.decode(data)
        self.chunk_z = Integer.decode(data)
        self.groundup_continuous = Boolean.decode(data)
        self.primary_bit_mask = VarInt.decode(data)
        self.size = VarInt.decode(data)
        self.chunk_sections = ReprList()

        for _ in range(16):
            if ((self.primary_bit_mask & (1 << _)) != 0):
                self.chunk_sections.append(ChunkSection340(
                    data,
                    session,
                ))
            else:
                self.chunk_sections.append(0)

        if (self.groundup_continuous):
            self.biomes = ReprList(repr=False)

            for _ in range(256):
                self.biomes.append(Byte.decode(data))

        self.number_block_entities = VarInt.decode(data)
        if (self.number_block_entities > 0):
            self.block_entities = NBT.decode(data)