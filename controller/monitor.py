from flask import Blueprint,request,flash,render_template,session
from controller.registerUrl import monitor
from sever.individuation import getWater, getFeet
from sever.monitorSever import getWaterLogsByUsername,getFeetLogsByUsername,turnOnWater,turnOffWater
from sever.userSever import getUserByUsername
from sever.alertServer import getAlert
from util.monitorHumiture import humidity,temperature

@monitor.route('/main',methods = ['get'])
def main():
    return render_template('monitor/main.html')

@monitor.route('/viewHumiture',methods = ['get'])
def viewHumiture():
    model={'temperature':temperature,'humidity':humidity}
    return render_template('monitor/humiture-info.html',model=model)

@monitor.route('/RealTimeMonitor')
def viewRealTime():
    return render_template('monitor/portlet-base.html')

@monitor.route('/humiture',methods = ['get'])
def getHumiture():
    realTimehumiturere = {
        'temperature':temperature,
        'humidity':humidity
    }
    print("jdiejdoejdoejdo")
    print(realTimehumiturere)
    return realTimehumiturere

@monitor.route('/viewFeetLog',methods = ['get'])
def viewFeetLogs():
    username = session.get('user').get('username')
    feetLogs = getFeetLogsByUsername(username)
    feets=getFeet(username)
    model = {'feetlogs':feetLogs,
             'feets':feets}

    print("model",model)
    return render_template('extendFunction/view-feet-logs.html',model = model)
@monitor.route('/viewWaterLog',methods = ['get'])
def viewWaterLogs():
    username = session.get('user').get('username')
    waterLogs = getWaterLogsByUsername(username)
    waters=getWater(username)
    print('controllWaterLogs',waterLogs)
    model = {'waterlogs':waterLogs ,'waters':waters}
    return render_template('extendFunction/view-water-log.html',model = model)

@monitor.route('/turnOnWater',methods = ['get'])
def turnonWater():
    username = session.get('user').get('username')
    user = getUserByUsername(username)
    if turnOnWater(user) == True:
        model={'message':'打开成功'}
    else:
        model={'message':'打开失败'}

    return render_template('extendFunction/manageEquipment.html',model = model)

@monitor.route('/turnOffWater',methods = ['get'])
def turnoffWater():
    username = session.get('user').get('username')
    user = getUserByUsername(username)
    if turnOffWater(user) == True:
        model={'message':'关闭成功'}
    else:
        model={'message':'关闭失败'}
    return render_template('extendFunction/manageEquipment.html',model = model)


@monitor.route('/manageEquipment',methods = ['get'])
def manageEquipment():
    return render_template('extendFunction/manageEquipment.html')

@monitor.route('/getAlertInfo',methods = ['get'])
def getAlertInfo():
    user=session.get('user')
    username=user.get('username')
    alerts=getAlert(username)
    print('alertLogs', alerts)
    model = {'alerts': alerts}
    return render_template('monitor/alert.html', model=model)

