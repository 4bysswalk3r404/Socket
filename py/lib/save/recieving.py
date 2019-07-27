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
    namebuffer = int(conn.recv(3).decode().strip())
    filepath = loc + conn.recv(namebuffer).decode()

    print("namebuffer: %s, filepath: %s" % (namebuffer, filepath))

    contents_buffer = int(conn.recv(9).decode().strip())
    print("recieving %s with a size of %s bytes" % (filepath, contents_buffer))

    tag = conn.recv(4).decode()
    print("tag: " + tag)

    b = ''
    contents = ""
    for i in range(contents_buffer):
        contents += conn.recv(contents_buffer).decode()
        conn.send("!*%6")
        #print("\r%s" % i, end="")
    tag = conn.recv(4).decode()
    print("tag: " + tag)

    string_data = ast.literal_eval(contents)
    int_data = [int(c) for c in string_data]
    bytes_data = bytes(int_data)
    with open(filepath, 'wb') as f:
        f.write(bytes_data)
    print('recieved %s with size of %s bytes' % (filepath, contentsbuffer))

def RecieveFolder(conn, loc=''):
    namebuffer = int(conn.recv(3).decode().strip())
    dirname = loc + conn.recv(namebuffer).decode()
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    print('(folder)', dirname)
    return dirname

def RecieveTree(conn):
    dir = input("Location of tree: ")
    foldernum = int(conn.recv(3).decode().strip())
    filenum = int(conn.recv(3).decode().strip())
    for _ in range(foldernum):
        RecieveFolder(conn, loc=dir)
    for _ in range(filenum):
        RecieveFile(conn, keep=True, loc=dir)
