import sys
if sys.platform == 'linux':
    sys.path.append("../lib")
    sys.path.append("./lib")
elif sys.platform == 'win32':
    sys.path.append("..\\lib")
    sys.path.append(".\\lib")

#from getIPs import getIPs
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Server ip: ")
PORT = 3702

client.connect((HOST, PORT))

while 1:
    data = input(">>>")
    #div = sys.getsizeof(data) // 126
    client.send(data.encode())
