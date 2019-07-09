import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("HOST: ")
PORT = 3702

data = input("Send: ")

s.connect((HOST, PORT))
print("connected")

data = s.send(data.encode())
print("sent")
