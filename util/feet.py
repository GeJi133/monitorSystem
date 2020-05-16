from threading import Thread, Timer
import datetime
from model.individuation import insertFeetLog, getFeetByUser
from model.modelDB import Feet
from .feetUtil import feet


class Feet(Thread):
    feet = None

    def run(self):
        while 1:
            if datetime.datetime.now() == feet.time:
                feet(feet)
                insertFeetLog(feet.username, datetime.datetime.now(), feet.amount, feet.petname, feet.category)

class TimingFeet(Thread):
    feet = None
    def run(self):
        feet(feet)
        insertFeetLog(feet.username, datetime.datetime.now(), feet.amount, feet.petname, feet.category)

def timingFeet(user):
    print("开始定时喂食")
    t2 = TimingFeet()
    t2.feet = getFeetByUser(user.username)
    t2.deamon = True  # 设置为守护线程
    t2.start()
    return True

def feet(user):
    print("现在喂食")
    t2 = Feet()
    t2.feet = getFeetByUser(user.username)
    t2.deamon = True  # 设置为守护线程
    t2.start()
    return True

def turnDownMonitor(event):
    event.clear()