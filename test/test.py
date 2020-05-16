from util.piConnection import turnOnCam,turnoffCam,getVedio,getHumiture,getConnection,closeConnection
from time import sleep

#建立socket连接
clientSocket = getConnection()
#调用piConnection里的方法
turnOnCam(clientSocket)
#断开socket连接
closeConnection(clientSocket)

print("hdjskfk")
sleep(20)
print("dsjkfk")

clientSocket = getConnection()
turnoffCam(clientSocket)
closeConnection(clientSocket)

clientSocket = getConnection()
getVedio(clientSocket)
closeConnection(clientSocket)

clientSocket = getConnection()
getHumiture(clientSocket)
closeConnection(clientSocket)