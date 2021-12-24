import random
from mcpi.minecraft import Minecraft
mc=Minecraft.create("anorfire.club")

uuid=mc.getPlayerEntityId("")
x, y, z=mc.entity.getTilePos(uuid)

for i in range(20):
    r = random.randrange(1,5)
    if r == 1:
        mc.setBlocks(x,y,z,x+4,y,z,1)
        x = x+4
    if r == 2:
        mc.setBlocks(x,y,z,x-4,y,z,41)
        x = x-4
