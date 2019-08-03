import sys
if sys.platform == 'linux':
    sys.path.append("./lib")
elif sys.platform == 'win32':
    sys.path.append("./lib")

import os
import socket
import caps
from recieving import *

serversock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sys.platform == 'win32':
    HOST = socket.gethostbyname(socket.gethostname())
else:
    HOST = input("HOST: ")
print(HOST)
PORT = 3704
serversock.bind((HOST, PORT))
serversock.listen(2)

#conn, addr
def serverAddClient(serversock, clientList):
    info = serversock.accept()
    clientList.append(info)
    print("connected to ", info[1])

clientList = []
serverAddClient(serversock, clientList)
serverAddClient(serversock, clientList)
clientList = dict(clientList)

while 1:
    recieveType = serversock.recv(1)

    if   recieveType == 1:
        serversockTransferString()
    elif recieveType == 2:
        serversockTransferFile()
