from encodings.utf_8 import encode
from socket import *

from pip._vendor.distlib.compat import raw_input

serverName = "192.168.0.106"
serverPort = 12002
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:').encode()
print("sentence",sentence)
clientSocket.send(sentence)
if sentence.decode() == "request video":
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
        print("data:",data)
        print("end:",end.encode())
        if data == end.encode():
            print("breask")
            break

    print("接受完毕")
    with open(file_path,'wb') as vedioFile:
        print("file_conet")
        vedioFile.write(total_data)
else:
    modifiedSentence = clientSocket.recv(2048).decode()
    print("From Server:", modifiedSentence )
clientSocket.close()