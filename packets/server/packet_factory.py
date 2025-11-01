from ...datatypes import *
from ..packet import Packet
from .status_response import ServerStatusResponsePacket340
from .status_pong import ServerStatusPongPacket340
from .set_compression import ServerSetCompressionPacket340
from .login_disconnect import ServerLoginDisconnectPacket340
from .login_success import ServerLoginSuccessPacket340
from .join_game import ServerJoinGamePacket340
from .plugin_message import ServerPluginMessagePacket340
from .server_difficulty import ServerServerDifficultyPacket340
from .player_abilities import ServerPlayerAbilitiesPacket340
from .held_item_change import ServerHeldItemChangePacket340
from .entity_status import ServerEntityStatusPacket340
from .unlock_recipes import ServerUnlockRecipesPacket340

from typing import Dict
import inspect

class ServerPacketFactory:
    def __init__(self):
        self.packets: Dict[int, Dict[int, Packet]] = {}

    def register(self, id: integer, state: integer, packet: Packet):
        self.packets[id] = self.packets.get(id, {})
        self.packets[id][state] = packet

    def create_packet(self, state: integer, data: bytes) -> Packet:
        data = bytearray(data)
        id = VarInt.from_bytes(data).inp

        kwargs: Dict[str, DataType] = {}
        for parameter in list(inspect.signature(self.packets[id][state].__init__).parameters.values())[1:]:
            kwargs[parameter.name] = parameter.annotation.from_bytes(data)

        return self.packets[id][state](**kwargs)
    
class ServerPacketFactory340(ServerPacketFactory):
    def __init__(self):
        super().__init__()

        self.register(0x00, 0x01, ServerStatusResponsePacket340)
        self.register(0x01, 0x01, ServerStatusPongPacket340)
        
        self.register(0x00, 0x02, ServerLoginDisconnectPacket340)
        self.register(0x02, 0x02, ServerLoginSuccessPacket340)
        self.register(0x03, 0x02, ServerSetCompressionPacket340)

        self.register(0x0d, 0x03, ServerServerDifficultyPacket340)
        self.register(0x18, 0x03, ServerPluginMessagePacket340)
        self.register(0x1b, 0x03, ServerEntityStatusPacket340)
        self.register(0x23, 0x03, ServerJoinGamePacket340)
        self.register(0x2c, 0x03, ServerPlayerAbilitiesPacket340)
        self.register(0x31, 0x03, ServerUnlockRecipesPacket340)
        self.register(0x3a, 0x03, ServerHeldItemChangePacket340)