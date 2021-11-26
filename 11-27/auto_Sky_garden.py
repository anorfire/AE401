from mcpi.minecraft import Minecraft
import random,time
block_type=0
mc = Minecraft.create("anorfire.club")
uuid=mc.getPlayerEntityId("Aphrodite32728")
x,y,z=mc.entity.getTilePos(uuid)

for i in range(0,20):
    mc.setBlocks(x,y-1+i,z+i,x+2,y-1+i,z+i,155)
    time.sleep(0.5)
    mc.entity.setTilePos(uuid,x+1,y+i,z+i)

x,y,z=mc.entity.getTilePos(uuid)
mc.setBlocks(x-3,y-1,z,x+3,y-1,z+6,2)
blockid=random.choice([37,38])
if blockid==38:
    block_type=random.randint(0,8)

mc.setBlocks(x-3,y,z,x+3,y,z+6,blockid,block_type)
