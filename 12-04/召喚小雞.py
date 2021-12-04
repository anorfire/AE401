from mcpi.minecraft import Minecraft
mc=Minecraft.create()

uuid=mc.getPlayerEntityId("Aphrodite32728")
x, y, z=mc.entity.getTilePos(uuid)

for i in range(5):
    mc.spawnEntity(x,y,z,93)
