from encodings.utf_8 import encode
from socket import *
#from pip._vendor.distlib.compat import raw_input

#建立连接
def getConnection():
    serverName = "30c7c19239.wicp.vip"
    serverPort = 22399
    clientSocket = socket(AF_INET, SOCK_STREAM)

    clientSocket.connect((serverName, serverPort))
    return clientSocket
#get视频
def getVedio(clientSocket):
    sentence = "request video"
    print("sentence",sentence)
    clientSocket.send(sentence.encode())
    print("From Server:wedio1")
    file_name = 'vedio1.h264'
    file_path = 'E:\\'+file_name
    total_data = b''
    num = 0
    data = clientSocket.recv(8388608)
    # total_data += data
    num = len(data)
    end = 'end'
    end.encode()
    while len(data)>0:
        print("接受视频数据")
        num += len(data)
        total_data += data
        print("接受前")
        data = clientSocket.recv(102400)
        print("datasize",len(data))
        if data == end.encode():
            print("breask")
            break

    print("接受完毕")
    with open(file_path,'wb') as vedioFile:
        print("file_conet")
        vedioFile.write(total_data)
    return file_path

#打开摄像头
def turnOnCam(clientSocket):
    sentence = "turn on camera"
    print("sentence", sentence)
    clientSocket.send(sentence.encode())
    print("发送信息",sentence)
    modifiedSentence = clientSocket.recv(2048).decode()
    print("From Server:", modifiedSentence)

#关闭摄像头
def turnoffCam(clientSocket):
    sentence = "turn off camera"
    print("sentence", sentence)
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(2048).decode()
    print("From Server:", modifiedSentence)

#得到温湿度
def getHumiture(clientSocket):
    sentence = "request humiture"
    print("sentence", sentence)
    clientSocket.send(sentence.encode())
    humiture = clientSocket.recv(2048).decode()
    print("From Server:", humiture)
    return humiture

def closeConnection(clientSocket):
    clientSocket.close()