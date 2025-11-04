from .network_client import *
from .packets import *
from .datatypes import *
from .dataclass import *

client = NetworkClient()
client.connect("localhost", 25565)

client.send_packet(ClientHandshakePacket340(
    protocol_version=340,
    server_address="127.0.0.1",
    server_port=25565,
    next_state=2,
))
client.set_state(2)
client.send_packet(ClientLoginStartPacket340(
    name="imbot",
))
print(client.get_packet())
client.set_state(3)
print(client.get_packet())
client.send_packet(ClientClientSettingsPacket340(
    locale="en_GB",
    view_distance=1,
    chat_mode=0,
    chat_colors=True,
    displayed_skin_parts=255,
    main_hand=1,
))
print(client.get_packet())
print(client.get_packet())
print(client.get_packet())
print(client.get_packet())
print(client.get_packet())
print(client.get_packet())
print(client.get_packet())
print(client.get_packet())
packet = client.get_packet()
while (True):
    print(type(packet))
    packet = client.get_packet()

while (type(packet) == ServerChunkDataPacket340 or
       type(packet) == ServerEntityPropertiesPacket340 or
       type(packet) == ServerEntityMetadataPacket340 or
       type(packet) == ServerSpawnMobPacket340 or
       type(packet) == ServerEntityEquipmentPacket340 or
       type(packet) == ServerSpawnObjectPacket340 or
       type(packet) == ServerEntityMetadataPacket340 or
       type(packet) == ServerEntityVelocityPacket340 or
       type(packet) == ServerPositionAndViewPacket340 or
       type(packet) == ServerWorldBorderPacket340 or
       type(packet) == ServerTimeUpdatePacket340 or
       type(packet) == ServerSpawnPositionPacket340 or
       type(packet) == ServerWindowItemsPacket340 or
       type(packet) == ServerChangeGameStatePacket340 or
       type(packet) == ServerSetSlotPacket340 or
       type(packet) == ServerAdvancementsPacket340 or
       type(packet) == ServerEntityRelativeMovePacket340 or
       type(packet) == ServerUpdateHealthPacket340 or
       type(packet) == ServerSetExperiencePacket340 or
       type(packet) == ServerKeepAlivePacket340 or
       type(packet) == ServerEntityLookAndRelativeMovePacket340 or
       type(packet) == ServerEntityHeadLookPacket340 or
       type(packet) == ServerEntityStatusPacket340 or
       type(packet) == ServerEntityTeleportPacket340):
    print(type(packet))
    packet = client.recv_packet()

print(packet)

data = bytearray(client.sock.recv(1024))
VarInt.decode(data)
print(data)