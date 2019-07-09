import socket
import sys

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Server ip: ")

client.connect((HOST, 3702))

while 1:
    data = input(">>>")
    #data_arr = []
    div = sys.getsizeof(data) // 2024
    client.send(data.encode())
