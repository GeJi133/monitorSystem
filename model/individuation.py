from .modelDB import *
def insertFeet(username, time, amount,petname ,category ):
    feet = Feet(username = username,time = time ,amount = amount,petname = petname,category = category)
    db.session.add(feet)
    db.session.commit()

def insertFeetLog(username, time, amount,petname ,category ):
    feetLog = FeetLog(username = username,time = time,amount = amount,petname = petname,category = category)
    db.session.add(feetLog)
    db.session.commit()

def insertWater(username, ontime, offtime ):
    water = Water(username = username,ontime = ontime,offtime = offtime)
    db.session.add(water)
    db.session.commit()

def insertWaterLog(username, time, opreation ):
    waterLog = WaterLog(username = username,time = time,operation=opreation)
    db.session.add(waterLog)
    db.session.commit()

def getWaterByUser(username):
    water=Water.query.filter_by(username = username).all()
    print('water',water)
    print(type(water))
    return water

def getWaterLogsByUser(username):
    waterLogs = WaterLog.query.filter_by(username = username).all()
    print("waterlogs",waterLogs)
    return waterLogs

def getFeetLogsByUser(username):
    feetLogs = FeetLog.query.filter_by(username = username).all()
    print("feetLogs",feetLogs)
    return feetLogs

def getFeetByUser(username):
    feet = Feet.query.filter_by(username=username).all()
    return feet

def insertIntoUser(username,password,dorId=None,phonenumber=None):
    user = User(username = username,password= password,dorId=dorId,phonenumber=phonenumber)
    db.session.add(user)
    db.session.commit()

def getUserByuserameAndPass(username,password):
    user = User.query.filter_by(username = username,password = password).first()
    return user

def getUserByuserame(username):
    user = User.query.filter_by(username = username).first()
    return user
def updateUser(username=None,password=None,dorId=None,phonenumber=None):
    user = User.query.filter_by(username = username).first()
    user.password = password
    user.dorId = dorId
    user.phonenumber = phonenumber
    db.session.commit()
def getSignOnByNameAndPass(username,password):
    signOn = SignOn.query.filter_by(username = username,password = password).first()
    return signOn