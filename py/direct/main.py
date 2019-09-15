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

    def listen(self):
        print(self.conn.recv(2048).decod())

class Client:
    def __init__(self, ThatIp):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def __call__(self):
        self.sock.connect((ThatIp, PORT))
        print("Client connected")

    def dispute(self):
        self.sock.send(input(">>>").encode())

if __name__ == "__main__":
    ThisIp = input("Your ip: ")
    ThatIp = input("Other ip: ")
