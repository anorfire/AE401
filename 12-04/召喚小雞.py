from mcpi.minecraft import Minecraft
mc=Minecraft.create()

uuid=mc.getPlayerEntityId("Aphrodite32728")
x, y, z=mc.entity.getTilePos(uuid)

for i in range(5):                              #使用條件迴圈執行五次召喚小雞
    mc.spawnEntity(x,y,z,93)                    #小雞ID:93
