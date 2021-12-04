from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        block=mc.getBlock(x,y,z)
        mc.setBlock(x,y,z,41)
        mc.postToChat("將原本方塊ID:" + str(block) + "變成金磚!")
