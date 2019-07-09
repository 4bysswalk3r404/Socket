import sys
if sys.platform == 'linux':
    sys.path.append("../lib")
elif sys.platform == 'win32':
    sys.path.append("..\\lib")

import socket
import BufferSplit

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Server ip: ")
PORT = 3702

client.connect((HOST, PORT))

while 1:
    data = input(">>>")
    command = data.split(' ')
    if command[0] == 'send':
        if command[1] == 'string':
            pass
        elif command[1] == 'file':
            pass
        elif command[1] == 'folder':
            pass
    dataVec = BufferVec(data)
    for data in dataVec:
        client.send(data)
