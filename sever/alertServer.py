from model.monitorDB import getAlertInfo,getAlertbyId
def getAlert(username):
    return getAlertInfo(username)
def getAlertById(id):
    return getAlertbyId(id)