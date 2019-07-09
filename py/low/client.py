import sys
sys.path.append("..\\lib")
sys.path.append(".\\lib")

from get_lan_ip import get_lan_ip
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Server ip: ")
PORT = 3702
if HOST == "":
    HOST = "192.168.86.168"

client.connect((HOST, PORT))

while 1:
    data = input(">>>")
    #div = sys.getsizeof(data) // 126
    client.send(data.encode())
