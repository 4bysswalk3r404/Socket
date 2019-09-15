import tkinter as tk
import threading
import random
import socket
import sys
import os

PORT = 3358

class Server:
    def __init__(self, ThisIp):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connInfo = None
        self.conn = None

    def __call__(self):
        self.sock.bind((ThisIp, PORT))
        self.sock.listen(1)
        self.conn, self.connInfo = self.sock.accept()
        print("Server connected", self.connInfo)
        while 1:
            print(self.sock.recv(2048).decode())

class Client:
    def __init__(self, ThatIp):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __call__(self):
        self.sock.connect((ThatIp, PORT))
        print("Client connected")
        while 1:
            self.sock.send(input(">>>").encode())

if __name__ == "__main__":
    ThisIp = input("Your ip: ")
    ThatIp = input("Other ip: ")

    server = Server(ThisIp)
    client = Client(ThatIp)

    threading.Thread(target=server)
    threading.Thread(target=client)
