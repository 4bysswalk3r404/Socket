import sys
if sys.platform == 'linux':
    sys.path.append("../../lib")
elif sys.platform == 'win32':
    sys.path.append("..\\..\\lib")

from BufferSplit import Vectorize
import caps
import os

def RecieveString(conn):
    data = conn.recv(64).decode()
    print('(string)' + caps.Snip(data, '(*s)'), end="")
    while not '(*s)' in data:
        data = conn.recv(64).decode()
        print(caps.Snip(data, '(*s)'), end="")
        if '(*s)' in data:
            print('|\n')
            return
    print('-\n')

def RecieveFile(conn):
    data = conn.recv(64).decode().split('(^f)')
    FileName = data[0]
    print("(file)", FileName)
    with open(FileName, 'w') as NewFile:
        NewFile.write(caps.Snip(data[1], '(*f)'))
        while not '(*f)' in data:
            data = conn.recv(128).decode()
            print(caps.Snip(data, '(*f)'), file=NewFile)
            if '(*f)' in data:
                return

#def RecieveFolder():
#    data = conn.recv(12)
#    while not caps.lastis(data, '</folder>'):
#        data = conn.recv(128).decode()
#        if caps.lastis(data, '</folder>'):
#            return
