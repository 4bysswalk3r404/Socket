import sys
import caps
import os

def RecieveString(conn):
    stringbuffer = int(conn.recv(5).strip())
    string = conn.recv(stringbuffer).decode()
    return string

def RecieveFile(conn, keep=False):
    namebuffer = int(conn.recv(3).decode().strip())
    filepath = conn.recv(namebuffer).decode()
    if not keep:
        filepath = os.path.basename(filepath)
    contentbuffer = int(conn.recv(5).decode().strip())
    contents = conn.recv(contentbuffer).decode()
    with open(filepath, 'w') as f:
        f.write(contents)
    return [filepath, contents]

def RecieveFolder(conn):
    namebuffer = int(conn.recv(3).decode().strip())
    dirname = conn.recv(namebuffer).decode()
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    return dirname

def RecieveTree(conn):
    foldernum = int(conn.recv(3).decode().strip())
    filenum = int(conn.recv(3).decode().strip())
    for _ in range(foldernum):
        RecieveFolder(conn)
    for _ in range(filenum):
        RecieveFile(conn)
