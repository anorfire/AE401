import time as t
from mcpi.minecraft import Minecraft
#----------------------------------------#

mc=Minecraft.create("anorfire.club",4711)

uuid=mc.getPlayerEntityId("Aphrodite32728")

Pos=mc.entity.getTilePos(uuid)

mc.entity.setTilePos(uuid,Pos.x,Pos.y,Pos.z)
t.sleep(0.5)
Pos.y=Pos.y+1

mc.entity.setTilePos(uuid,Pos.x,Pos.y,Pos.z)
t.sleep(0.5)
Pos.y=Pos.y+1

mc.entity.setTilePos(uuid,Pos.x,Pos.y,Pos.z)