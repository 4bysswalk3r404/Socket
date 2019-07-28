import sys
import caps
import os
import random
import encrypt

def SendData(client, data):
    #get random seed, charcoal it, send it
    seed = random.randrange(16777216)
    charredSeed = encrypt.charcoal(seed, 3)
    client.send(charredSeed)

    #encrypt data and Vectorize it
    encrypted = encrypt.encrypt(data)
    encryptedVec = caps.Vectorize(encrypted)

    #get base length of buffer array
    basebufferlen = len(encryptedVec) - 1
    basebufferlen = caps.Fill(encrypt.BytesEncode(basebufferlen), 10)

    #get buffer length of last element
    endbufferlen = len(encryptedVec[::-1])
    endbufferlen = caps.Fill(encrypt.BytesEncode(endbufferlen), 4)

    #send basebufferlen and endbufferlen
    client.send(basebufferlen)
    client.send(endbufferlen)

    for chunk in encryptedVec:
        client.send(chunk)
        pause = client.recv(1)
        if pause != b'\x00':
            print('error')

def SendString(client, string):
    client.send(b'\x01')
    SendData(client, encrypt.BytesEncode(string))

def SendFile(client, filename):
    if not os.path.exists(filename):
        print(FileExistsError)
        return
    client.send(b'\x02')

    filenamebuffer = encrypt.BytesEncode(str(len(filename)))
    client.send(caps.Fill(filenamebuffer, 3))
    client.send(encrypt.BytesEncode(filename))

    data = open(filename, 'rb').read()
    SendData(client, data)
