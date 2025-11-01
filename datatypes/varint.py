from .datatype import DataType

class VarInt(DataType):
    def __init__(self, num: int):
        super().__init__(num)

    @classmethod
    def from_bytes(cls, data: bytearray):
        shift = 0
        decoded = 0

        while (True):
            i = data.pop(0)
            decoded |= (i & 0x7f) << shift
            shift += 7
            if (not (i & 0x80)):
                break

        return cls(decoded)

    def encode(self) -> bytes:
        number = self.inp
        encoded = bytearray()

        while True:
            byte = number & 0x7F
            number >>= 7

            if number > 0: byte |= 0x80
            encoded.append(byte)
            
            if number == 0:
                break
                
        return bytes(encoded)