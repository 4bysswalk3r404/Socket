import sys
import caps
import os

def SendString(client, string):
    client.send('(&s)'.encode())
    client.send(caps.Fill(str(len(string)), 5).encode())
    client.send(string.encode())

def SendFile(client, filepath):
    if not os.path.exists(filepath):
        print(FileNotFoundError)
        return
    client.send('(&f)'.encode())
    client.send(caps.Fill(str(len(filepath)), 3).encode())
    client.send(filepath.encode())
    data = open(filepath, 'rb').read()
    string_data = [str(int(b)) for b in data]
    client.send(caps.Fill(str(len(str(string_data))), 5).encode())
    client.send(string_data)
    print("sent %s with length of %s bytes" % (filepath, len(str(string_data))))

def SendFolder(client, dir):
    client.send('(&d)'.encode())
    client.send(caps.Fill(str(len(dir)), 3).encode())
    client.send(dir.encode())

def SendTree(client, dir):
    client.send('(&t)'.encode())
    folders = [path.replace(dir, '.') for sub in [[os.path.join(w[0], file) for file in w[1]] for w in os.walk(dir)] for path in sub]
    files = [path.replace(dir, '.') for sub in [[os.path.join(w[0], file) for file in w[2]] for w in os.walk(dir)] for path in sub]
    client.send(caps.Fill(str(len(folders)), 3))
    client.send(caps.Fill(str(len(files)), 3))
    for folder in folders:
        SendFolder(client, folder)
    for file in files:
        SendFile(client, file)

def close(client):
    client.send('(!!)'.encode())
    sys.exit()
