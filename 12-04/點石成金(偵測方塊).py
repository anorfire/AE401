from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    hits = mc.events.pollBlockHits()                #偵測使用劍點左鍵 
    if len(hits)>0:                                 #判斷是否取得到hits
        hit = hits[0]                               #將取得道的hit[0]放進hit
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z       #獲得x,y,z位置
        block=mc.getBlock(x,y,z)                    #獲取方塊ID
        mc.postToChat("獵到的方塊:"+str(block))
