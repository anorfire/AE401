# 這是AE401教室的上課內容

  程式學習需要持之以恆，持續練習也是非常重要的一環，家長需要的話可以與孩子一起研究程式!

常見指令:
mc=Minecraft.create("anorfire.club")          #引號內可換成自己的伺服器ip \
uuid=mc.getPlayerEntityId("玩家ID")   
x, y, z=mc.entity.getTilePos(uuid)            #從getPlayerEntityId取得道的id
mc.entity.setTilePos(uuid, x, y, z)           #設定玩家座標
mc.setBlock(x, y, z ,方塊數字ID)
mc.getBlock(x, y, z )                         #獲取方塊數字ID
mc.postToChat("")                             #將引號內輸入的內容傳送到伺服器聊天室



待補
