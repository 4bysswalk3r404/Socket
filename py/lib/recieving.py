import sys
import caps
import os
import random
import encrypt
import gzip
import zlib

#compression is broken
def ReceiveData(conn, safe=True, compression=False):
    charredSeed = conn.recv(3)
    seed = encrypt.uncharcoal(charredSeed)

    basebufferlen = int(encrypt.BytesDecode(caps.Strip(conn.recv(10))))
    endbufferlen = int(encrypt.BytesDecode(caps.Strip(conn.recv(4))))
    buffers = [1000 for _ in range(basebufferlen)]
    buffers.append(endbufferlen)

    data = b''
    for buffer in buffers:
        chunk = conn.recv(buffer)
        data += chunk
        conn.send(b'\x00')
    if compression:
        data = zlib.decompress(data)
    return encrypt.decrypt(data, seed)

def RecieveString(conn):
    string = encrypt.BytesDecode(ReceiveData(conn))
    print('(string)%s' % string)

def RecieveFile(conn):
    filenamebuffer = encrypt.BytesDecode(caps.Strip(conn.recv(3)))
    filename = encrypt.BytesDecode(conn.recv(int(filenamebuffer)))

    filename = os.path.basename(filename)

    data = ReceiveData(conn)
    with open(filename, 'wb') as file:
        file.write(data)
    print("recieved %s with size of %s" % (filename, len(data)))
