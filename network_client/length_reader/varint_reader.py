from .length_reader import LengthReader


class VarIntLengthReader(LengthReader):
    @staticmethod
    def read_length(connection):
        shift = 0
        decoded = 0

        while (True):
            i = int.from_bytes(connection.recv(1))
            decoded |= (i & 0x7f) << shift
            shift += 7
            if (not (i & 0x80)):
                break

        return decoded