import socket
import threading
import time
import queue
import curses

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("HOST: ")
PORT = int(input("PORT: "))

server = server.bind((HOST, PORT))
client = client.connect((HOST, PORT))

def recieve(q):
    data = server.recv(1024)
    if data:
        return data

def send(q):
    data = input(">>>")

stdscr = curses.initscr()
maxY, maxX = stdscr.getmaxyx()

def main():
    stdscr.clear()
