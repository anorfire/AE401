from mcpi.minecraft import Minecraft
import random,time
block_type=0                                        #初始化方塊Type，用於判斷ID:38的花朵
mc = Minecraft.create("anorfire.club")              #Minecraft.create與老師的伺服器建立連線
uuid=mc.getPlayerEntityId("Aphrodite32728")         #獲取玩家的ID並存到變數UUID
x,y,z=mc.entity.getTilePos(uuid)                    #獲取玩家座標並存到變數x、y、z
 
for i in range(0,20):                               #設定條件式迴圈(這裡會輸出數字0到19)
    mc.setBlocks(x,y-1+i,z+i,x+2,y-1+i,z+i,155)     #mc.setblocks(x座標,y座標-1+迴圈數字i,z+迴圈數字i,x+2,y-1+迴圈數字i,z+迴圈數字i,方塊id)
    time.sleep(0.5)                                 #使程式休息一下
    mc.entity.setTilePos(uuid,x+1,y+i,z+i)          #設定玩家座標使玩家能夠自動上樓梯 mc.entity.setTilePos(玩家uuid,座標)

x,y,z=mc.entity.getTilePos(uuid)                    #重新獲取玩家上完樓梯後的座標x、y、z
mc.setBlocks(x-3,y-1,z,x+3,y-1,z+6,2)               #創造花園的平台
blockid=random.choice([37,38])                      #隨機選擇ID:37或38的花朵
if blockid==38:                                     #如果隨機選到38的花朵，在選一次38的type
    block_type=random.randint(0,8)

mc.setBlocks(x-3,y,z,x+3,y,z+6,blockid,block_type)  #將上面選擇出來的花放在平台上
