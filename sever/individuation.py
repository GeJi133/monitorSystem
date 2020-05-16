from model.individuation import insertWaterLog,insertFeetLog,getWaterByUser,getFeetByUser,getFeetLogsByUser,getWaterLogsByUser
from util.feet import feet, timingFeet
from util.water import waterOn,waterOff, timingWater


def getFeetLogsByUsername(username):
    feetlogs = getFeetLogsByUser(username)
    return feetlogs
def getWaterLogsByUsername(username):
    waterlogs = getWaterLogsByUser(username)
    return waterlogs
def getWaterLogsByUsername(username):
    waterlogs = getWaterLogsByUser(username)
    return waterlogs
def startTimingFeet(user):
    return timingFeet(user)
def startTimingWater(user):
    return timingWater(user)
def turnOnWater(user):
    return waterOn(user)
def turnOffWater(user):
    return waterOff(user)
def getFeet(username):
    return getFeetByUser(username)
def getWater(username):
    return getWaterByUser(username)






