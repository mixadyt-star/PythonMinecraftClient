from .packets import *

import socket

class NetworkClient:
    def __init__(self, server_factory: ServerPacketFactory):
        self.connected = False
        self.state = 0
        self.server_factory = server_factory
        self.sock = socket.socket()

    def connect(self,
                server_address: str,
                server_port: int):

        self.sock.connect((
            self.parse_server_address(server_address),
            server_port
        ))
        self.connected = True

    def send_packet(self, packet: Packet):
        if (self.connected):
            self.sock.send(packet.craft().pack())
        else:
            raise RuntimeError("Client not connected")

    def recv_packet(self) -> Packet:
        if (self.connected):
            return self.server_factory.create_packet(self.state, self.sock.recv(self.recv_length()))
        else:
            raise RuntimeError("Client not connected")

    def recv_length(self) -> int:
        shift = 0
        decoded = 0

        while (True):
            i = int.from_bytes(self.sock.recv(1))
            decoded |= (i & 0x7f) << shift
            shift += 7
            if (not (i & 0x80)):
                break

        return decoded

    def set_state(self, state: int):
        self.state = state

    @staticmethod
    def parse_server_address(server_address):
        try:
            socket.inet_pton(socket.AF_INET, server_address)
            return server_address
        except socket.error:
            try:
                return socket.gethostbyname(server_address)
            except socket.gaierror:
                raise ValueError("Invalid address")