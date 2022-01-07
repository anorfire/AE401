import random
from mcpi.minecraft import Minecraft

mc = Minecraft.create("anorfire.club")
uuid = mc.getPlayerEntityId("Aphrodite32728")
x,y,z = mc.entity.getTilePos(uuid)
r = random.randrange(1,16)

while 1:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        hit = hits[0]
        
        block = mc.getBlockWithData(hit.pos)
        data = block.data
        if data == r:
            mc.postToChat("猜對了唷!!")
            mc.setBlock(hit.pos,57)
        elif data < r:
            mc.postToChat("猜錯了唷!! 往更大的id猜看看")
        elif data > r:
            mc.postToChat("猜錯了唷!! 往更小的id猜看看")
