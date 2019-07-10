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

def SendString(data):
    dataVec = Vectorize(data)
    for data in dataVec:
        client.send(data)

def SendFile(File):
    client.send('<file>'.encode())
    fn, ex = os.path.splitext(File)
    client.send(fn.encode())
    client.send(ex.encode())

    dataVec = Vectorize(open(File, 'r').read())
    for data in dataVec:
        client.send(data)
    client.send('</file>')

def SendFolder(Folder):
    client.send('<folder>')
    #not implemented
    client.send('</folder>')

protocol = 'string'
while 1:
    data = input('(%s)' % protocol)
    command = data.split(' ')
    if command[0] == 'use':
        if command[1] == 'string':
            protocol = 'string'
        elif command[1] == 'file':
            protocol = 'file'
        elif command[1] == 'folder':
            protocol = 'folder'
    else:
        if protocol == 'string':
            SendString(data)
        elif protocol == 'file':
            SendFile(data)
        elif protocol == 'folder':
            SendFolder(data)
