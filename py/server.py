import sys
if sys.platform == 'linux':
    sys.path.append("./lib")
elif sys.platform == 'win32':
    sys.path.append("./lib")

import os
import socket
import caps
from recieving import *

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sys.platform == 'win32':
    HOST = socket.gethostbyname(socket.gethostname())
else:
    HOST = input("HOST: ")
print(HOST)
PORT = 3702
server.bind((HOST, PORT))
server.listen(1)
conn, addr = server.accept()
print("connected to ", addr)

while 1:
    data = conn.recv(1)
    if data == b'\x01':
        RecieveString(conn)
    elif data == b'\x02':
        RecieveFile(conn)
