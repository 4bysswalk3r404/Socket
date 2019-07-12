import sys
import socket
import time
import threading
from getch import getch

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Other ip: ")

server.bind(('localhost', 3702))
client.connect((HOST, 3702))

class glob:
    self.rc = None
    self.out = None

def reciever():
    while 1:
        try:
            data = server.recv(2024)
            glob.rc = data
        except Exception as e:
            glob.rc = e

def sender():
    while 1:
        c = None
        data = None
        while ord(c) != 10:
            c = getch()
            if ord(c) == 3:
                sys.exit()
            data += c
        glob.out = data

def main():
    while 1:
        if glob.rc != None:
            print(glob.rc)
        if glob.out != None:
            client.send(glob.out)
        glob.rc = None
        glob.out = None

threading.Thread(reciever)
threading.Thread(sender)
main()
