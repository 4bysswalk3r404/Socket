import sys
import caps
import os
import random
import encrypt

def ReceiveData(conn, safe=True):
    charredSeed = conn.recv(3)
    seed = encrypt.uncharcoal(charredSeed)

    charredBBL = conn.recv(4)
    charredEBL = conn.recv(2)
    basebufferlen = encrypt.uncharcoal(charredBBL)
    endbufferlen = encrypt.uncharcoal(charredBBL)
    buffers = [1000 for _ in range(basebufferlen)]
    buffers.append(endbufferlen)

    data = b''
    for buffer in buffers:
        chunk = conn.recv(buffer)
        data += chunk
        conn.send(b'\x00')
    return encrypt.decrypt(data, seed)

def RecieveString(conn):
    string = encrypt.BytesDecode(ReceiveData(conn))
    print('(string)%s' % string)

def RecieveFile(conn):
    filenamebuffer = encrypt.uncharcoal(conn.recv(1))
    filename = encrypt.BytesDecode(conn.recv(filenamebuffer))

    filename = os.path.basename(filename)

    data = ReceiveData(conn)
    with open(filename, 'wb') as file:
        file.write(data)
    print("recieved %s with size of %s" % (filename, len(data)))
