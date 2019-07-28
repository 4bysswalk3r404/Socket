import sys
import caps
import os
import random
import encrypt

def ReceiveData(conn, safe=True):
    charredSeed = conn.recv(3)
    seed = encrypt.uncharcoal(charredSeed)

    basebufferlen = int(encrypt.BytesDecode(caps.Strip(conn.recv(10))))
    endbufferlen = int(encrypt.BytesDecode(caps.Strip(conn.recv(4))))
    buffers = [1000 for _ in range(basebufferlen)]
    buffers.append(endbufferlen)

    data = b''
    for i, buffer in enumerate(buffers):
        chunk = conn.recv(buffer)
        print("\r%i" % i, end="")
        data += encrypt.decrypt(chunk, seed)
        conn.send(b'\x00')
    print()
    return data

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
