from .datatype import DataType
from .utils import *

from io import BytesIO
from pynbt import *


class NBT(DataType):
    @staticmethod
    def encode(data: NBTFile):
        file = BytesIO()
        data.write(file)

        return file.getvalue()
    
    @staticmethod
    def decode(data) -> NBTFile:
        file = BytesIO(data)

        return NBTFile(file)