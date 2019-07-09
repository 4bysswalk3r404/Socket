import socket
import time
import threading

server = socket.socket(socket.AF_INIT, socket.SOCK_STREAM)
client = socket.socket(socket.AF_INIT, socket.SOCK_STREAM)

HOST = input("Other ip: ")

server.bind(('localhost', 3702))
client.connect((HOST, 3702))

class glob:
    pass

def reciever():
    while 1:
        try:
            data = server.recv(2024).decode('utf-8')
            glob.in = [data, time.time()]
        except Exception as e:
            glob.in = [e, time.time()]

def sender():
    while 1:
        client.send(data)

def main():
    pass

threading.Thread(reciever)
threading.Thread(sender)
threading.Thread(main)
