import sys
import os
sys.path.append('./lib')

from sending import *
from recieving import *
import threading
import socket

svSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

if sys.platform == 'win32':
    HOST = socket.gethostbyname(socket.gethostname())
else:
    HOST = input("HOST: ")
PORT = 3702

svSock.bind((HOST, PORT))
clSock.connect((HOST, PORT))

def client():
    pass

def server():
    pass

cl = threading.Thread(client)
sv = threading.Thread(server)

cl.start()
vs.start()
