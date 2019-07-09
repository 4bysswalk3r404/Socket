import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 3702

s.bind((HOST, PORT))
print("connected")

data = s.recv(1024).decode('utf-8')
print(data)
