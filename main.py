from .network_client import NetworkClient
from .packets import *
from .datatypes import *

client = NetworkClient(server_factory=ServerPacketFactory340())
client.connect("localhost", 25565)

client.send_packet(ClientHandshakePacket340(
    protocol_version=VarInt(340),
    server_address=String("127.0.0.1"),
    server_port=UnsignedShort(25565),
    next_state=VarInt(2),
))
client.set_state(2)
client.send_packet(ClientLoginStartPacket340(
    name=String("imbot"),
))
print(client.recv_packet())
client.set_state(3)
print(client.recv_packet())
client.send_packet(ClientClientSettingsPacket340(
    locale=String("en_GB"),
    view_distance=Byte(1),
    chat_mode=VarInt(0),
    chat_colors=Boolean(True),
    displayed_skin_parts=UnsignedByte(255),
    main_hand=VarInt(1),
))
print(client.recv_packet())
print(client.recv_packet())
print(client.recv_packet())
print(client.recv_packet())
print(client.recv_packet())
print(client.recv_packet())
print(client.sock.recv(1024))