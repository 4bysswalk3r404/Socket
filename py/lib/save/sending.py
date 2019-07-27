import sys
import caps
import os

def SendString(client, string):
    client.send('(&s)'.encode())
    client.send(caps.Fill(str(len(string)), 5).encode())
    client.send(string.encode())

def SendFile(client, filepath):
    client.send('(&f)'.encode())

    filepath_buffer = caps.Fill(str(len(filepath)), 3)
    client.send(filepath_buffer.encode())
    client.send(filepath.encode())

    contents = open(filepath, 'rb').read()
    string_data = [str(int(b)) for b in contents]

    dataVec = caps.Vectorize(string_data, 1000)

    contents_buffer = caps.Fill(str(len(dataVec)), 9)
    client.send(contents_buffer.encode())

    client.send("(&b)".encode())
    for chunk in contentbuffer:
        client.send(chunk)
    client.send("(*b)".encode())
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
