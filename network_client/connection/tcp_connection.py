from .connection import Connection
from ..address_parser import *

import socket


class TcpConnection(Connection):
    def __init__(self, address_parser: AddressParser):
        self.address_parser = address_parser
        self.socket = socket.socket()
        self._connected = False

    def connect(self, address, port):
        parsed_address = self.address_parser.parse(address)
        self.socket.connect((parsed_address, port))
        self._connected = True

    def send(self, data):
        if (not self._connected):
            raise RuntimeError("Client not connected")
        
        self.socket.send(data)

    def recv(self, length):
        if (not self._connected):
            raise RuntimeError("Client not connected")
        
        return self.socket.recv(length)
    
    def close(self):
        self.socket.close()
        self._connected = False

    @property
    def connected(self) -> bool:
        return self._connected