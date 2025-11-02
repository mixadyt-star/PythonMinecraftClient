from abc import *


class AddressParser(ABC):
    @abstractmethod
    def parse(self, address: str) -> str: ...