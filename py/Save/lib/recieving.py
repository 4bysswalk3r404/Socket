import sys
import caps
import os
import random
import encrypt

def ReceiveData(conn, datatype=bytes, protected=True):
    #recieve seed
    if protected:
        chared = conn.recv(6).decode()
        seed = encrypt.uncharcoal(chared)

    #recieve base array size and end array buffer size
    baselen = int(conn.recv(7).decode().strip())
    endlen  = int(conn.recv(3).decode().strip())

    #recieve all the data!!!
    data = []
    for i in range(baselen):
        chunk = conn.recv(1000)
        if protected:
            data.append(encrypt.decrypt(chunk, seed, datatype))
        else:
            data.append(chunk)
        conn.send(b'\x00')
    chunk = conn.recv(endlen)
    if protected:
        data.append(encrypt.decrypt(chunk, seed, datatype))
    else:
        data.append(chunk)
    conn.send(b'\x00')
    if datatype is bytes:
        return ''.join(data).encode()
    elif datatype is str:
        return ''.join(data)

def RecieveString(conn):
    string = ReceiveData(conn, str)
    print('(string)', string)

def ReceiveFileUnprotected(conn):
    #recieve filename buffer and filename
    filename_buffer = int(conn.recv(2).decode().strip())
    filename = conn.recv(filename_buffer).decode()

    #get contents and write it to file
    contents = ReceiveData(conn, protected=False)
    with open(filename, "wb") as file:
        file.write(contents)
    print("received %s with size of %s bytes" % (filename, len(contents)))

def RecieveFile(conn, keep=False, loc=''):
    #recieve filename buffer and filename
    filename_buffer = int(conn.recv(2).decode().strip())
    filename = conn.recv(filename_buffer).decode()

    #get contents and write it to file
    contents = ReceiveData(conn)
    with open(filename, "wb") as file:
        file.write(contents)
    print("received %s with size of %s bytes" % (filename, len(contents)))
