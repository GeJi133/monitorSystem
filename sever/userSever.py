from model.userDB import insertIntoUser,inserIntoSignOn,getUserByuserameAndPass,getUserByuserame
from model.modelDB import *


def getUserByNameAndPass(username,password):
    return getUserByuserameAndPass(username,password)
def getUserByUsername(username):
    return getUserByuserame(username)

def insertUser(username,password,dorId=None,phonenumber=None):
    insertIntoUser(username,password,dorId,phonenumber)

