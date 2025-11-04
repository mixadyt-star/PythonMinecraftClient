from .address_parser import *
from .automatic_receiver import *
from .connection import *
from .length_reader import *
from .packet_processor import *
from .packet_queue import *
from .state_manager import *
from ..packets import *
from ..dataclass import Session

from typing import *


class NetworkClient:
    def __init__(self, automatic_receiver: Optional[AutomaticPacketReceiver] = None):
        self.automatic_receiver = automatic_receiver or DefaultAutomaticPacketReceiver(
            connection=TcpConnection(
                address_parser=DefaultAddressParser(),
            ),
            state_manager=LockedStateManager(),
            packet_processor=ServerPacketProcessor(
                server_factory=ServerPacketFactory340(
                    session=Session(),
                ),
            ),
            queue_manager=ServerPacketQueueManager(),
            length_reader=VarIntLengthReader(),
        )

    def connect(self,
                server_address: str,
                port: int):
        
        self.automatic_receiver.connection.connect(
            server_address,
            port,
        )
        self.automatic_receiver.start()

    def close(self):
        self.automatic_receiver.stop()
        self.automatic_receiver.connection.close()

    def send_packet(self, packet: ClientPacket):
        self.automatic_receiver.connection.send(
            data=packet.pack(),
        )

    def get_packet(self) -> ServerPacket:
        return self.automatic_receiver.queue_manager.get_packet()
    
    def has_packets(self) -> bool:
        return self.automatic_receiver.queue_manager.has_packets()
    
    def set_state(self, state: int):
        self.automatic_receiver.state_manager.state = state
    
