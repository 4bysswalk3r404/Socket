import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('localhost', 135))
server.listen(1)

conn, addr = server.accept()

while 1:
    data = conn.recv(2024).decode()
    print(data)
