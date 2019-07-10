import sys
if sys.platform == 'linux':
    sys.path.append("../../lib")
elif sys.platform == 'win32':
    sys.path.append("..\\..\\lib")

from BufferSplit import Vectorize
import caps
import os

def RecieveString(conn):
    data = conn.recv(128).decode()
    print(data, end="")
    while not '(*s)' in data:
        data = con.recv(128).decode()
        print(data, end="")
        if '(*s)' in data:
            print('\n')
            return

def RecieveFile(conn):
    FileName = conn.recv(64).decode().replace(' ', '')
    data = ""
    with open(FileName, 'w') as NewFile:
        while not '(*f)' in data:
            data = conn.recv(128).decode()
            if '(*f)' in data):
                return
            print(data, file=NewFile)

#def RecieveFolder():
#    data = conn.recv(12)
#    while not caps.lastis(data, '</folder>'):
#        data = conn.recv(128).decode()
#        if caps.lastis(data, '</folder>'):
#            return
