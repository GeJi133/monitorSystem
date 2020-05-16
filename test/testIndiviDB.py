import datetime
import time
from model.individuation import insertFeetLog, insertWaterLog, insertWater, insertFeet, getFeetByUser, getWaterByUser, \
    getWaterLogsByUser, getFeetLogByUser

now = datetime.datetime.now()

time = datetime.timedelta(hours = 12,minutes=3,seconds=30)
#insertWaterLog('pp', now, 'yibing' )
print("time",time)
print('datatime',now.time())
#insertWater('mm',time, '777' )
#insertFeetLog('ppp', now, "amount","petname" ,"category" )
#insertFeet("lll", time, "amount","petname" ,"category" )
waterlog = getWaterLogByUser('aa')
print('water',waterlog)
water = getWaterByUser('aa')
print(water.username)
feetLog=getFeetLogByUser('aa')
print(feetLog.category)
feet = getFeetByUser('aa')
print(feet.amount)

