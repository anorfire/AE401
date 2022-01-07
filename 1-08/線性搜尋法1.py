from time import time
r=100
sTime = time()
for i in range(1001):
    if r == i:
        print("找到了!答案是:"+str(i))
        print("線性搜尋法花了:"+str(time()-sTime)+"秒")
        break
