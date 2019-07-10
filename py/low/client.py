import sys
if sys.platform == 'linux':
    sys.path.append("../lib")
elif sys.platform == 'win32':
    sys.path.append("..\\lib")

import os
import socket
import BufferSplit

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Server ip: ")
PORT = 3702

client.connect((HOST, PORT))

protocol = 'string'
while 1:
    data = input('(%s)' % protocol)
    command = data.split(' ')
    if command[0] == 'use':
        if command[1] == 'string':
            protocol = 'string'
        elif command[1] == 'file':
            protocol = 'file'
    else:
        if protocol == 'string':
            SendString(client, data)
        elif protocol == 'file':
            SendFile(client, data)
