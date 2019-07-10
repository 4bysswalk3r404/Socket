import sys
import caps

def Vectorize(data, buffer=128):
    dataVec = []
    charArr = []
    data = data[::-1]
    while data:
        if sys.getsizeof("".join(charArr).encode()) < buffer:
            charArr.append(data[-1])
        if sys.getsizeof("".join(charArr).encode()) > buffer:
            charArr = charArr[:-1]
            dataVec.append("".join(charArr).encode())
            charArr = []
        else:
            data = data[:-1]
    if charArr:
        dataVec.append(caps.Fill("".join(charArr), 128).encode())
    return dataVec

if __name__ == "__main__":
    mult = int(input("mult: "))
    data = 'a'*mult
    print(Vectorize(data))
