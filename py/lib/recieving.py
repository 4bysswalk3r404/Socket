import sys
import caps
import os
import ast

def RecieveString(conn):
    stringbuffer = int(conn.recv(5).strip())
    string = conn.recv(stringbuffer).decode()
    print('(string)', string)
    return string

def RecieveFile(conn, keep=False, loc=''):
    #recieve filename buffer and filename
    filename_buffer = int(conn.recv(2).strip().decode())
    filename = conn.recv(filename_buffer).decode()

    #recieve base array size and end array buffer size
    baselen = int(conn.recv(7).strip().decode())
    endlen  = int(conn.recv(3).strip().decode())

    #recieve file contents in 1000 size buffers
    contents = []
    for _ in range(baselen):
        chunk = conn.recv(1000)
        conn.send(b'$')
        contents.append(chunk)
    chunk = conn.recv(endlen)
    contents.append(chunk)

    #write to file
    with open(filename, "wb") as file:
        for chunk in contents:
            file.write(chunk)
