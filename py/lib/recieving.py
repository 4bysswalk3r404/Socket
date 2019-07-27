import sys
import caps
import os
import ast
import random
import encrypt

def ReceiveData(conn):
    #recieve seed
    seed = int(conn.recv(6).decode().strip())

    #recieve base array size and end array buffer size
    baselen = int(conn.recv(7).decode().strip())
    endlen  = int(conn.recv(3).decode().strip())

    contents = []
    for _ in range(baselen):
        chunk = encrypt.decrypt(conn.recv(1000), seed)
        contents.append(chunk)
        conn.send(b'$')
    chunk = encrypt.decrypt(conn.recv(endlen), seed)
    contents.append(chunk)
    conn.send(b'$')
    return ''.join(contents)

def RecieveString(conn):
    #recieve seed
    chared = conn.recv(6).decode()
    seed = encrypt.uncharcoal(chared)

    #recieve encrypted string and decrypt it
    stringbuffer = int(conn.recv(6).decode().strip())
    encrypted = conn.recv(stringbuffer).decode()
    decrypted = encrypt.decrypt(encrypted, seed)

    print('(string)', decrypted)

def RecieveFile(conn, keep=False, loc=''):
    #recieve filename buffer and filename
    filename_buffer = int(conn.recv(2).decode().strip())
    filename = conn.recv(filename_buffer).decode()

    #recieve base array size and end array buffer size
    baselen = int(conn.recv(7).decode().strip())
    endlen  = int(conn.recv(3).decode().strip())

    #recieve file contents in 1000 size buffers
    contents = []
    for _ in range(baselen):
        chunk = conn.recv(1000)
        contents.append(chunk)
        conn.send(b'$')
    chunk = conn.recv(endlen)
    contents.append(chunk)
    conn.send(b'$')

    #write to file
    with open(filename, "wb") as file:
        for chunk in contents:
            file.write(chunk)
    print("received %s with size of %s bytes" % (filename, (baselen * 1000) + endlen))
