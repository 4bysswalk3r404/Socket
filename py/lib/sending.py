import sys
from BufferSplit import Vectorize
import caps
import os

def SendString(client, string):
    client.send('(&s)'.encode())
    client.send(caps.Fill(str(len(string)), 5).encode())
    client.send(string.encode())

def SendFile(client, filepath):
    if not os.path.exists(filepath):
        print(FileNotFoundError)
        break
    client.send('(&f)'.encode())
    client.send(caps.Fill(str(len(filepath)), 3).encode())

    filename = os.basename(filepath)
    client.send(filename.encode())

    data = open(filepath, 'r')
    client.send(caps.Fill(str(len(data)), 5).encode())
    client.send(data.encode())
