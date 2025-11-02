from .packet_queue import PacketQueueManager

from queue import *


class ServerPacketQueueManager(PacketQueueManager):
    def __init__(self):
        self.queue = Queue()

    def put_packet(self, packet):
        self.queue.put(packet)

    def get_packet(self):
        return self.queue.get()
    
    def has_packets(self):
        return not self.queue.empty()