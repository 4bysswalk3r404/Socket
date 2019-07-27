import random
import caps

def encrypt(buffer, seed, datatype=str):
    random.seed(seed)
    encrypted = []
    if datatype is str:
        for c in buffer:
            encrypted.append(chr((ord(c) + random.randrange(256)) % 256))
    elif datatype is bytes:
        for c in buffer:
            encrypted.append(chr((c + random.randrange(256)) % 256))
    return ''.join(encrypted).encode()

def decrypt(buffer, seed, datatype=str):
    random.seed(seed)
    encrypted = []
    if datatype is str:
        for c in buffer:
            encrypted.append(chr((ord(c) - random.randrange(256)) % 256))
    elif dataype is bytes:
        for c in buffer:
            encrypted.append(chr((c - random.randrange(256)) % 256))
    return ''.join(encrypted)

def binaryToDecimal(n):
    return int(n, 2)

def decimalToBinary(n):
    return caps.ZeroFill(bin(n).replace("0b",""), 4)

def charcoal(num):
    binary = caps.ZeroFill(decimalToBinary(num), 24)
    binvec = caps.Vectorize(binary, 4)
    return ''.join([chr(binaryToDecimal(bin)) for bin in binvec])

def uncharcoal(chararr):
    bin = ""
    for char in chararr:
        bin += decimalToBinary(ord(char))
    return binaryToDecimal(bin)

if __name__ == "__main__":
    num = int(input("num: "))
    coal = charcoal(num, 3)
    print(uncharcoal(coal, 3))
