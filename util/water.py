from threading import Thread, Timer
import datetime
from model.individuation import insertWaterLog, getWaterByUser
from model.modelDB import Water
from .waterUtil import turnOnWater, turnOffWater, turnOffWaterNow, turnOnWaterNow


class TimingWater(Thread):
    water = None

    def run(self):
        while 1:
            if datetime.datetime.now() == water.ontime:
                turnOnWater(water)
                insertWaterLog(water.username, datetime.datetime.now(), 'turnOn')
            if datetime.datetime.now() == water.offtime:
                turnOffWater()
                insertWaterLog(water.username, datetime.datetime.now(), 'turnOff')


class WaterOn(Thread):
    user = None

    def run(self):
        if turnOnWaterNow(user)==True:
            insertWaterLog(user.username, datetime.datetime.now(), 'turnOn')


class WaterOff(Thread):
    user = None

    def run(self):
        if turnOffWaterNow(user) == True:
            insertWaterLog(user.username, datetime.datetime.now(), 'turnOff')


def timingWater(user):
    print("开始定时开启饮水机")
    t2 = TimingWater()
    t2.water = getWaterByUser(user.username)
    t2.deamon = True  # 设置为守护线程
    t2.start()
    return True


def waterOn(user):
    print("开启饮水机")
    t2 = WaterOn()
    t2.water = getWaterByUser(user.username)
    t2.deamon = True  # 设置为守护线程
    t2.start()
    return True

def waterOff(user):
    print("关闭饮水机")
    t2 = WaterOff()
    t2.water = getWaterByUser(user.username)
    t2.deamon = True  # 设置为守护线程
    t2.start()
    return True
