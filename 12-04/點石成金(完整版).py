from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()                                #偵測使用劍點左鍵
    if len(hits)>0:                                                 #判斷是否取得到hits
        hit = hits[0]                                               #將取得道的hit[0]放進hit
        x, y, z = hit.pos.x, hit.pos.y, hit.pos.z                   #獲得x,y,z位置
        block=mc.getBlock(x,y,z)                                    #獲得block ID
        mc.setBlock(x,y,z,41)                                       #將獲取的位置改變成金磚
        mc.postToChat("將原本方塊ID:" + str(block) + "變成金磚!")
