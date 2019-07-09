import sys
sys.path.append("..\\lib")
sys.path.append(".\\lib")

from get_lan_ip import get_lan_ip
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = get_lan_ip()
PORT = 3702

server.bind((HOST, PORT))
server.listen(1)

conn, addr = server.accept()

while 1:
    data = conn.recv(126).decode()
    print(data)
