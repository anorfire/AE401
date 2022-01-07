import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create("anorfire.club")
uuid = mc.getPlayerEntityId("Aphrodite32728")
x,y,z = mc.entity.getTilePos(uuid)

for i in range(10):
    for j in range(10):
        r = random.randrange(0,16)
        mc.setBlock(x+i,y,z+j,35,r)
