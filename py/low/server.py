import sys
if sys.platform == 'linux':
    sys.path.append("../lib")
    sys.path.append("./lib")
elif sys.platform == 'win32':
    sys.path.append("..\\lib")
    sys.path.append(".\\lib")

import os
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("HOST: ")
PORT = 3702

server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()
print("connected to ", addr)

def RecieveFile():
    FileName = conn.recv(126).decode()
    extension = conn.recv(126).decode()
    with open(FileName + extension, 'w') as NewFile:
        while data != '</file>':
            data = conn.recv(126).decode()
            if data == '</file>':
                return
            print(data, file=NewFile)

def RecieveFolder():
    while data != '</folder>':
        data = conn.recv(126).decode()
        if data == '</folder>':
            return

protocol = 'string'
while 1:
    data = conn.recv(126).decode()
    if data == '<file>':
        RecieveFile()
    elif data == '<folder>':
        RecieveFolder()
    print('(%s)' % protocol, data)
    if data == 'close':
        break
