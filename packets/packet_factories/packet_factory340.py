from .packet_factory import ServerPacketFactory
from ..server import *


class ServerPacketFactory340(ServerPacketFactory):
    def __init__(self, session):
        super().__init__(session)

        self.register(0x00, 0x01, ServerStatusResponsePacket340)
        self.register(0x01, 0x01, ServerStatusPongPacket340)
        
        self.register(0x00, 0x02, ServerLoginDisconnectPacket340)
        self.register(0x02, 0x02, ServerLoginSuccessPacket340)
        self.register(0x03, 0x02, ServerSetCompressionPacket340)

        self.register(0x00, 0x03, ServerSpawnObjectPacket340)
        self.register(0x03, 0x03, ServerSpawnMobPacket340)
        self.register(0x0d, 0x03, ServerServerDifficultyPacket340)
        self.register(0x14, 0x03, ServerWindowItemsPacket340)
        self.register(0x16, 0x03, ServerSetSlotPacket340)
        self.register(0x18, 0x03, ServerPluginMessagePacket340)
        self.register(0x1b, 0x03, ServerEntityStatusPacket340)
        self.register(0x1e, 0x03, ServerChangeGameStatePacket340)
        self.register(0x1f, 0x03, ServerKeepAlivePacket340)
        self.register(0x20, 0x03, ServerChunkDataPacket340)
        self.register(0x23, 0x03, ServerJoinGamePacket340)
        self.register(0x26, 0x03, ServerEntityRelativeMovePacket340)
        self.register(0x27, 0x03, ServerEntityLookAndRelativeMovePacket340)
        self.register(0x29, 0x03, ServerVehicleMovePacket340)
        self.register(0x2c, 0x03, ServerPlayerAbilitiesPacket340)
        self.register(0x2e, 0x03, ServerPlayerListItemPacket340)
        self.register(0x2f, 0x03, ServerPositionAndViewPacket340)
        self.register(0x31, 0x03, ServerUnlockRecipesPacket340)
        self.register(0x36, 0x03, ServerEntityHeadLookPacket340)
        self.register(0x38, 0x03, ServerWorldBorderPacket340)
        self.register(0x3a, 0x03, ServerHeldItemChangePacket340)
        self.register(0x3c, 0x03, ServerEntityMetadataPacket340)
        self.register(0x3e, 0x03, ServerEntityVelocityPacket340)
        self.register(0x3f, 0x03, ServerEntityEquipmentPacket340)
        self.register(0x40, 0x03, ServerSetExperiencePacket340)
        self.register(0x41, 0x03, ServerUpdateHealthPacket340)
        self.register(0x46, 0x03, ServerSpawnPositionPacket340)
        self.register(0x47, 0x03, ServerTimeUpdatePacket340)
        self.register(0x4c, 0x03, ServerEntityTeleportPacket340)
        self.register(0x4d, 0x03, ServerAdvancementsPacket340)
        self.register(0x4e, 0x03, ServerEntityPropertiesPacket340)