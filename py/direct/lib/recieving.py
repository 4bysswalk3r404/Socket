import sys
import os
import random
import encrypt
import zlib

def _RecieveDataSmall(conn):
    seed = int.from_bytes(conn.recv(3), 'big')
    databuffer = int.from_bytes(conn.recv(1), 'big')
    data = encrypt.decrypt(conn.recv(databuffer), seed)
    return data

def ReceiveData(conn, compress=False):
    seed = int.from_bytes(conn.recv(3), 'big')

    basebufferlen = int.from_bytes(conn.recv(4), 'big')
    endbufferlen = int.from_bytes(conn.recv(2), 'big')
    buffers = [1000 for _ in range(basebufferlen)]
    buffers.append(endbufferlen)

    data = b''
    for buffer in buffers:
        chunk = conn.recv(buffer)
        data += chunk
        conn.send(b'\x00')

    decrypted = encrypt.decrypt(data, seed)
    if compress:
        return zlib.decompress(decrypted)
    else:
        return decrypted

def RecieveString(conn):
    string = encrypt.BytesDecode(ReceiveData(conn))
    print('(string)%s' % string)

def RecieveFile(conn):
    filename = encrypt.BytesDecode(_RecieveDataSmall(conn))
    filename = os.path.basename(filename)

    data = ReceiveData(conn, True)
    with open(filename, 'wb') as file:
        file.write(data)
    print("recieved %s with size of %s" % (filename, len(data)))

def RecieveFolder(conn):
    foldername = _RecieveDataSmall(conn)
    if not os.path.exists(foldername):
        os.makedirs(foldername)
