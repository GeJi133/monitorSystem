from .modelDB import *
def getAlertInfo(username):
    alerts = Alert.query.filter_by(username = username).all()
    print("waterlogs",alerts)
    return alerts