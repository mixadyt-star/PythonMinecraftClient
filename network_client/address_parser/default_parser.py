from .address_parser import AddressParser

import socket


class DefaultAddressParser(AddressParser):
    def parse(self, address):
        try:
            socket.inet_pton(socket.AF_INET, address)
            return address
        except socket.error:
            try:
                return socket.gethostbyname(address)
            except socket.gaierror:
                raise ValueError("Invalid address")