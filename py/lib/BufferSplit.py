import sys
import caps

def Vectorize(data, buffer=128):
    dataVec = []
    charArr = []
    data = data[::-1]
    while data:
        if sys.getsizeof("".join(charArr).encode()) < buffer:
            charArr.append(data[-1])
            data = data[:-1]
        else:
            dataVec.append("".join(charArr).encode())
            charArr = []
    if charArr:
        dataVec.append(caps.Fill("".join(charArr), 64).encode())
    return dataVec

if __name__ == "__main__":
    data = str(input(">>>"))
    print(Vectorize(data))
