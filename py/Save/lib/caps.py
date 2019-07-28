import sys

def lastis(string, sub):
    string = string[::-1]
    sub = sub[::-1]
    matched = 0
    for i in len(sub):
        if sub[i] == string[i]:
            matched += 1
    if matched == len(sub):
        return True
    else:
        return False

def Fill(data, buffsize=32):
    if not type(data) is str:
        string = str(data)
    else:
        string = data
    return string + (' ' * (buffsize - len(string)))

def ZeroFill(string, buffsize):
    return ('0' * (buffsize - len(string))) + string

def Snip(string, cap):
    if cap in string:
        return string[:len(string)-len(cap)].strip()
    else:
        return string.strip()

def Vectorize(bytes, buffer=1000):
    return [bytes[x:x+buffer] for x in range(0, len(bytes), buffer)]
