#from app import clientSocket
from util.piConnection import getHumiture, turnOnCam, turnoffCam
from util.piConnection import getHumiture,getConnection,closeConnection
import json
from time import sleep
from flask import session
# encoding:utf-8
# Author:"richie"
# Date:8/29/2017
# python线程：线程的调度-守护线程

from threading import Thread,Timer
import time

from util.sendMessage import send_sms

temperature = [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]
humidity = [7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 26.5, 23.3, 18.3, 13.9, 9.6]

class MyCommon(Thread):
    def run(self):
        # for i in range(1,5):
        #     t = Timer(7, self.print_msg, args=(i,))
        #     t.start()
        # 建立socket连接
        clientSocket = getConnection()
        # 调用piConnection里的方法
        turnOnCam(clientSocket)
        # 断开socket连接
        closeConnection(clientSocket)

        print("hdjskfk")
        sleep(30)
        print("dsjkfk")

        clientSocket = getConnection()
        turnoffCam(clientSocket)
        closeConnection(clientSocket)
        print("线程1第" ,"次执行！")

class MyDaemon(Thread):
    """
    守护线程不可以在重新new thread
    """
    def run(self):

        for i in range(9999999):
            connection = getConnection()
            humiture = getHumiture(connection)
            humiture = json.loads(humiture)
            print(type(humiture))
            print(humiture)
            closeConnection(connection)
            #if humiture[0]>30 or humiture[1]>=70:
            if i == 3:
                template = {
                    'code': '556634',
                }
                res = send_sms(template, phone='18956778851')
                print(str(res, encoding='utf-8'))
                res_dict = json.loads(res)
                if res_dict.get('Message') == 'OK' and res_dict.get('Code') == 'OK':
                    print("成功啦")
                else:
                    print("失败啦")
                t1 = MyCommon()
                t1.deamon = True
                print("正在录像")

                t1.start()

            temperature[i%12] = humiture[0]
            humidity[i%12] = humiture[1]

            print("后台线程第" + str(i) + "次执行！",humiture,temperature,humidity)
            time.sleep(5)


def turnOnMonitor():

    print("开启线程")
    t2 = MyDaemon()
    t2.deamon = True  # 设置为守护线程
    t2.start()

def turnDownMonitor(event):
    event.clear()