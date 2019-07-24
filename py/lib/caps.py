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

def Fill(string, bufsize=32):
    return string + (' ' * (bufsize - len(string)))

def Snip(string, cap):
    if cap in string:
        return string[:len(string)-len(cap)].strip()
    else:
        return string.strip()

def Vectorize(string, buffer=1000):
    vec = []
    while string:
        vec.append(string[:buffer])
        string = string[buffer:]
    if len(vec[-1] != buffer):
        vec[-1] = Fill(vec[-1], buffer)
    return vec
