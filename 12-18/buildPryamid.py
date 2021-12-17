from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def buildPryamid(x,y,z):
    base = 10
    height = (base//2)+1
    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        z2 = z + base - i
        mc.setBlocks(x1, y1 ,z1 ,x2 ,y ,z2, 24)

Name = input("請輸入遊戲ID：")
uuid = mc.getPlayerEntityId(Name)  #獲得uuid

x,y,z = mc.entity.getTilePos(uuid) #獲得x,y,z
buildPryamid(x,y,z)                #給副程式位置
mc.postToChat("玩家" + mc.entity.getName(uuid) + "在X= " + str(x) + " Y= " + str(y) + " Z= " + str(z) +"蓋了一個金字塔" )
