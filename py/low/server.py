import sys
if sys.platform == 'linux':
    sys.path.append("../lib")
    sys.path.append("./lib")
elif sys.platform == 'win32':
    sys.path.append("..\\lib")
    sys.path.append("./lib")

import os
import socket
import caps
from recieving import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = input("HOST: ")
PORT = 3702
server.bind((HOST, PORT))
server.listen(1)
conn, addr = server.accept()
print("connected to ", addr)

while 1:
    data = conn.recv(32).decode()
    if '(&s)' in data:
        print('string')
        RecieveString(conn)
    elif '(&f)' in data:
        print('file')
        RecieveFile(conn)
    if '(!!)' in data:
        break
