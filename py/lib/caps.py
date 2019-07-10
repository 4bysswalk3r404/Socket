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
    return string + (' ' * (bufsize - sys.getsizeof(string)))
