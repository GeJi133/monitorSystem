from .modelDB import *
def getAlertInfo(username):
    alerts = Alert.query.filter_by(username = username).all()
    print("aleerts",alerts)
    return alerts
def getAlertbyId(id):
    print(id)
    alert = Alert.query.filter_by(id = id).first()
    print("aleert",alert)
    return alert