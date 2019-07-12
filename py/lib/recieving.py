import sys
from BufferSplit import Vectorize
import caps
import os

def RecieveString(conn):
    stringbuffer = int(conn.recv(5).strip())
    string = conn.recv(stringbuffer).decode()
    return string

def RecieveFile(conn):
    namebuffer = int(conn.recv(3).decode().strip())
    filename = conn.recv(namebuffer).decode()
    contentbuffer = int(conn.recv(5).decode().strip())
    contents = conn.recv(contentbuffer).decode()
    return [filename, contents]
