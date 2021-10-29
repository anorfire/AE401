import time as t

from mcpi.minecraft import Minecraft
#----------------------------------------#

mc=Minecraft.create("anorfire.club",4711)

uuid=mc.getPlayerEntityId("Aphrodite32728")

Pos=mc.entity.getTilePos(uuid)

while 1:
    mc.postToChat("You are located on X:"+str(Pos.x)+",Y:"+str(Pos.y)+",Z"+str(Pos.z))
    t.sleep(0.5)

