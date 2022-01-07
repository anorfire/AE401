from time import time
r=5000
sTime = time() 
low = 0
upper = 10000
while low <= upper:
    mid = (low+upper) // 2 #無條件捨棄的除法 
    if mid < r:
        low = mid + 1
    elif mid > r:
        upper = mid - 1
    else :
        print("找到答案了！ 是" + str(mid))
        print("二元搜尋法：花了" + str(time()-sTime)) #計算程式花費時間(結束減開始)
        break
