import sys
if sys.platform == 'linux':
    sys.path.append("../../lib")
elif sys.platform == 'win32':
    sys.path.append("..\\..\\lib")

from BufferSplit import Vectorize
import caps
import os

def SendString(client, data):
    client.send(caps.Fill('(&s)').encode())
    dataVec = Vectorize(data)
    print(dataVec)
    for data in dataVec:
        client.send(data)
    client.send(caps.Fill('(*s)').encode())

def SendFile(client, FileName):
    if not os.path.exists(FileName):
        print(FileNotFoundError)
    dataVec = Vectorize(open(FileName, 'r').read())
    FileName = os.path.basename(FileName)
    FileName = caps.Fill(FileName+'(^f)', 64)
    client.send(caps.Fill('(&f)').encode())
    client.send(FileName.encode())

    for data in dataVec:
        client.send(data)
    client.send(caps.Fill('(*f)').encode())

#def SendFolder():
#    pass
#
#def SendTree():
#    pass
