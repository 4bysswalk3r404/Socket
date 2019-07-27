import sys
import caps
import os

def SendString(client, string):
    client.send('(&s)'.encode())
    client.send(caps.Fill(str(len(string)), 5).encode())
    client.send(string.encode())

def SendFile(client, filename):
    #make sure file exists
    if not os.path.exists(filename):
        print(FileExistsError)

    #send initializing file send/recieve code
    client.send("(&f)".encode())

    #send filename buffer and filename
    client.send(str(len(filename)).encode())
    client.send(filename.encode())

    #read file in binary format
    contents = open(filename, "rb").read()
    binaryvec = caps.Vectorize(contents)

    #send array size - 1 and buffer size of last element
    client.send(caps.Fill(len(binaryvec)-1, 7).encode())
    client.send(caps.Fill(len(binaryvec[-1]), 3).encode())

    #loop through array, sending the buffer
    for chunk in binaryvec:
        client.send(chunk)
