from .protocol import Protocol
from ....packets import *
from ....enums import *


class DefaultProtocol(Protocol):
    def __init__(self):
        self.register(State.STATUS, 0x00, ServerStatusResponsePacket340)
        self.register(State.STATUS, 0x01, ServerStatusPongPacket340)
        
        self.register(State.LOGIN, 0x00, ServerLoginDisconnectPacket340)
        self.register(State.LOGIN, 0x02, ServerLoginSuccessPacket340)
        self.register(State.LOGIN, 0x03, ServerSetCompressionPacket340)

        self.register(State.PLAY, 0x00, ServerSpawnObjectPacket340)
        self.register(State.PLAY, 0x03, ServerSpawnMobPacket340)
        self.register(State.PLAY, 0x0d, ServerServerDifficultyPacket340)
        self.register(State.PLAY, 0x14, ServerWindowItemsPacket340)
        self.register(State.PLAY, 0x16, ServerSetSlotPacket340)
        self.register(State.PLAY, 0x18, ServerPluginMessagePacket340)
        self.register(State.PLAY, 0x1b, ServerEntityStatusPacket340)
        self.register(State.PLAY, 0x1e, ServerChangeGameStatePacket340)
        self.register(State.PLAY, 0x1f, ServerKeepAlivePacket340)
        self.register(State.PLAY, 0x20, ServerChunkDataPacket340)
        self.register(State.PLAY, 0x23, ServerJoinGamePacket340)
        self.register(State.PLAY, 0x26, ServerEntityRelativeMovePacket340)
        self.register(State.PLAY, 0x27, ServerEntityLookAndRelativeMovePacket340)
        self.register(State.PLAY, 0x29, ServerVehicleMovePacket340)
        self.register(State.PLAY, 0x2c, ServerPlayerAbilitiesPacket340)
        self.register(State.PLAY, 0x2e, ServerPlayerListItemPacket340)
        self.register(State.PLAY, 0x2f, ServerPositionAndViewPacket340)
        self.register(State.PLAY, 0x31, ServerUnlockRecipesPacket340)
        self.register(State.PLAY, 0x36, ServerEntityHeadLookPacket340)
        self.register(State.PLAY, 0x38, ServerWorldBorderPacket340)
        self.register(State.PLAY, 0x3a, ServerHeldItemChangePacket340)
        self.register(State.PLAY, 0x3c, ServerEntityMetadataPacket340)
        self.register(State.PLAY, 0x3e, ServerEntityVelocityPacket340)
        self.register(State.PLAY, 0x3f, ServerEntityEquipmentPacket340)
        self.register(State.PLAY, 0x40, ServerSetExperiencePacket340)
        self.register(State.PLAY, 0x41, ServerUpdateHealthPacket340)
        self.register(State.PLAY, 0x46, ServerSpawnPositionPacket340)
        self.register(State.PLAY, 0x47, ServerTimeUpdatePacket340)
        self.register(State.PLAY, 0x4c, ServerEntityTeleportPacket340)
        self.register(State.PLAY, 0x4d, ServerAdvancementsPacket340)
        self.register(State.PLAY, 0x4e, ServerEntityPropertiesPacket340)