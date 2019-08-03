import sys
import caps
import os
import random
import encrypt
import zlib

def _RecieveDataSmall(serversock):
    seed = encrypt.uncharcoal(serversock.recv(3))
    databuffer = encrypt.uncharcoal(serversock.recv(1))
    data = encrypt.decrypt(serversock.recv(databuffer), seed)
    return data

def ReceiveData(serversock, compress=False):
    charredSeed = serversock.recv(3)
    seed = encrypt.uncharcoal(charredSeed)

    charredBBL = serversock.recv(4)
    charredEBL = serversock.recv(2)
    basebufferlen = encrypt.uncharcoal(charredBBL)
    endbufferlen = encrypt.uncharcoal(charredEBL)
    buffers = [1000 for _ in range(basebufferlen)]
    buffers.append(endbufferlen)

    data = b''
    for buffer in buffers:
        chunk = serversock.recv(buffer)
        data += chunk
        serversock.send(b'\x00')

    decrypted = encrypt.decrypt(data, seed)
    if compress:
        return zlib.decompress(decrypted)
    else:
        return decrypted

def RecieveString(serversock):
    addr = encrypt.BytesDecode(caps.Strip(serversock.recv(18)))
    return encrypt.BytesDecode(ReceiveData(serversock)), addr

def RecieveFile(serversock):
    addr = encrypt.BytesDecode(caps.Strip(serversock.recv(18)))

    filename = encrypt.BytesDecode(_RecieveDataSmall(serversock))
    filename = os.path.basename(filename)

    return filename, addr, ReceiveData(serversock, True)
