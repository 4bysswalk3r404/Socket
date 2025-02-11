import sys
import os
import random
import encrypt
import zlib

def _SendDataSmall(client, data):
    client.send(random.getrandbits(8*4).to_bytes(4, 'big'))
    client.send(len(data).to_bytes(1, 'big'))
    client.send(encrypt.encrypt(data, seed))

def SendData(client, data, compress=False):
    #get random seed, charcoal it, send it
    seed = random.getrandbits(8*4)
    client.send(seed.to_bytes(4, 'big'))

    if compress:
        data = zlib.compress(data)

    #encrypt data and Vectorize it
    encrypted = encrypt.encrypt(data, seed)
    encryptedVec = caps.Vectorize(encrypted)

    #send basebufferlen and endbufferlen
    client.send(len(basebufferlen).to_bytes(4, 'big'))
    client.send(len(endbufferlen).to_bytes(2, 'big'))

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

    _SendDataSmall(client, encrypt.BytesEncode(filename))

    data = open(filename, 'rb').read()
    SendData(client, data, True)
    print("sent %s with size of %s bytes" % (filename, len(data)))

def SendTree(client, treename):
    files = [path for sub in [[os.path.join(w[0], file) for file in w[2]] for w in os.walk(treename)] for path in sub]
    folders = [path[0] for path in os.walk(treename)]
    for folder in folders:
        SendFolder(client, folder)
    for file in files:
        SendFile(client, file)

def SendFolder(client, foldername):
    client.send(b'\x03')
    _SendDataSmall(client, encrypt.BytesEncode(foldername))
