from mcpi.minecraft import Minecraft
mc=Minecraft.create()

uuid=mc.getPlayerEntityId("Aphrodite32728")
x, y, z=mc.entity.getTilePos(uuid)

for i in range(5):                        #雙重迴圈 一排=5隻小雞
    for j in range(5):
        mc.spawnEntity(x+i, y+10, z+j,93)
