import sys
import caps
import os
import random
import encrypt

def SendData(client, data, datatype=bytes):
    #get seed, char it, send it
    seed = random.randrange(16777216)
    chared = encrypt.charcoal(seed)
    client.send(chared.encode())

    #encrypt data and Vectorize it
    encrypted = encrypt.encrypt(data, seed, datatype)
    encryptedvec = caps.Vectorize(encrypted)

    #send array size - 1 and buffer size of last element
    client.send(caps.Fill(len(encryptedvec)-1, 7).encode())
    client.send(caps.Fill(len(encryptedvec[-1]), 3).encode())

    #send all the data!!!
    for chunk in encryptedvec:
        client.send(chunk)
        pause = client.recv(1)
        if pause != b'$':
            print("error: ", pause)

def SendString(client, string):
    client.send(b'(&s)')
    SendData(client, string, str)

def SendFile(client, filename):
    #make sure file exists
    if not os.path.exists(filename):
        print(FileExistsError)
        return

    #send initializing file send/recieve code
    client.send(b"(&f)")

    #send filename buffer and filename
    client.send(caps.Fill(len(filename), 2).encode())
    client.send(filename.encode())

    #read file in binary format and give it to SendData
    contents = open(filename, "rb").read()
    SendData(client, contents)

    print("sent %s with a size of %s bytes" % (filename, len(contents)))
