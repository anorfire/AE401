# 這是AE401教室的上課內容

  程式學習需要持之以恆，持續練習也是非常重要的一環，家長需要的話可以與孩子一起研究程式!

常見指令:
 - mc = Minecraft.create("anorfire.club")          #雙引號內可換成自己的伺服器ip 
 - uuid = mc.getPlayerEntityId("玩家ID")            #獲得玩家在伺服器中的uuid，並存到uuid變數中
 - x, y, z = mc.entity.getTilePos(uuid)            #從getPlayerEntityId取得到的id，並存到x、y、z變數中
 - mc.entity.setTilePos(uuid, x, y, z)           #改變或設定玩家座標
 - mc.setBlock(x, y, z, 方塊數字ID)               #改變或設定該座標的方塊
 - mc.getBlock(x, y, z)                         #獲取方塊數字ID
 - mc.postToChat("")                             #將雙引號內輸入的內容傳送到伺服器聊天室
 - mc.spawnEntity(x, y, z, 生物數字ID)            #在座標上產生生物


待補
