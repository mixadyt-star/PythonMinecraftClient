from .automatic_receiver import AutomaticPacketReceiver
from ..packet_processor import *
from ..state_manager import *
from ..length_reader import *
from ..packet_queue import *
from ..connection import *

from concurrent.futures import ThreadPoolExecutor
from threading import *
from typing import *


class DefaultAutomaticPacketReceiver(AutomaticPacketReceiver):
    def __init__(self,
                 connection: Connection,
                 state_manager: StateManager,
                 packet_processor: PacketProcessor,
                 queue_manager: PacketQueueManager,
                 length_reader: LengthReader,
                 max_workers: int = 5):
        
        self.connection = connection
        self.state_manager = state_manager
        self.packet_processor = packet_processor
        self.queue_manager = queue_manager
        self.length_reader = length_reader

        self.thread_pool = ThreadPoolExecutor(max_workers=max_workers)
        self._receiving = False
        self._receive_thread: Optional[Thread] = None

    def start(self):
        if (not self.connection.connected):
            raise RuntimeError("Client not connected")
        
        self._receiving = True
        self._receive_thread = Thread(
            target=self._receive_loop,
            daemon=True
        )
        self._receive_thread.start()

    def stop(self):
        self._receiving = False
        if (self._receive_thread and self._receive_thread.is_alive()):
            self._receive_thread.join(timeout=1.0)

        self.thread_pool.shutdown(wait=False)

    def _receive_loop(self):
        while (self._receiving and self.connection.connected):
            length = self.length_reader.read_length(self.connection)
            data = self.connection.recv(length)

            if (data):
                self.thread_pool.submit(
                    self._process_packet,
                    data
                )

    def _process_packet(self, data: bytes):
        state = self.state_manager.state
        packet = self.packet_processor.process_packet(data, state)

        self.queue_manager.put_packet(packet)