import sys
import caps
import os
import random
import encrypt

def SendData(client, data):
    #get and send random seed
    seed = random.randrange(999999)
    client.send(caps.Fill(seed, 6).encode())

    #encrypt the data and Vectorize it
    encrypted = encrypt.encrypt(data, seed)
    binaryvec = caps.Vectorize(encrypted)

    #send array size - 1 and buffer size of last element
    client.send(caps.Fill(len(binaryvec)-1, 7).encode())
    client.send(caps.Fill(len(binaryvec[-1]), 3).encode())

    #loop through array, sending the buffer
    for chunk in binaryvec:
        client.send(chunk)
        pause = client.recv(1)
        if pause != b'$':
            print("error")

def SendString(client, string):
    client.send(b'(&s)')
    #get and send random seed
    seed = random.randrange(999999)
    client.send(caps.Fill(seed, 6).encode())

    #send encrypted string
    encrypted = encrypt.encrypt(string, seed)
    client.send(caps.Fill(len(encrypted), 6).encode())
    client.send(encrypted)

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

    #read file in binary format and Vectorize it
    contents = open(filename, "rb").read()
    binaryvec = caps.Vectorize(contents)

    #send array size - 1 and buffer size of last element
    client.send(caps.Fill(len(binaryvec)-1, 7).encode())
    client.send(caps.Fill(len(binaryvec[-1]), 3).encode())

    #loop through array, sending the buffer
    for chunk in binaryvec:
        client.send(chunk)
        pause = client.recv(1)
        if pause != b'$':
            print("error")
    print("sent %s with a size of %s bytes" % (filename, len(contents)))
