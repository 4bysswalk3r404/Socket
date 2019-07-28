import sys
import caps
import os
import random
import encrypt

def ReceiveData(conn):
    charredSeed = conn.recv(3)
    seed = encrypt.uncharred(charredSeed)

    basebufferlen = int(encrypt.BytesDecode(caps.Strip(conn.recv(10))))
    endbufferlen = int(encrypt.BytesDecode(caps.Strip(conn.recv(4))))

    data = b''
    for i in range(basebufferlen):
        chunk = conn.recv(1000)
        data += encrypt.decrypt(chunk, seed)
        conn.send(b'\x00')
    chunk = conn.recv(endbufferlen)
    data += encrypt.decrypt(chunk, seed)
    conn.send(b'\x00')

    return data

def ReceiveString(conn):
    string = encrypt.BytesDecode(ReceiveData(conn))
    print('(string)', string)

def RecieveFile(conn):
    filenamebuffer = encrypt.BytesDecode(caps.Strip(conn.recv(3)))
    filename = conn.recv(int(filenamebuffer))

    data = ReceiveData(conn)
    with open(filename, 'wb') as file:
        file.write(data)
