import sys

def Fill(data, buffsize=32):
    return data + (b'\x00' * (buffsize - len(data)))

def ZeroFill(string, buffsize):
    return ('0' * (buffsize - len(string))) + string

def Strip(data):
    for n in data[::-1]:
        if n == 0:
            data = data[:-1]
        else:
            return data

def Vectorize(bytes, buffer=1000):
    return [bytes[x:x+buffer] for x in range(0, len(bytes), buffer)]
