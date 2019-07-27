import random
import caps

def _encryptBytes(buffer, seed):
    random.seed(seed)
    encrypted = []
    for c in buffer:
        encrypted.append(chr((c + random.randrange(128)) % 128))
    return ''.join(encrypted)

def _decryptBytes(buffer, seed):
    random.seed(seed)
    decrypted = []
    for c in buffer:
        decrypted.append(chr((c - random.randrange(128)) % 128))
    return ''.join(decrypted)

def _encryptStr(buffer, seed):
    random.seed(seed)
    encrypted = []
    for c in buffer:
        encrypted.append(chr((ord(c) + random.randrange(256)) % 256))
    return ''.join(encrypted).encode()

def _decryptStr(buffer, seed):
    random.seed(seed)
    decrypted = []
    for c in buffer:
        decrypted.append(chr((ord(c) - random.randrange(256)) % 256))
    return ''.join(decrypted)

def encrypt(buffer, seed, datatype):
    if datatype is str:
        return _encryptStr(buffer, seed)
    elif datatype is bytes:
        return _encryptBytes(buffer, seed)

def decrypt(buffer, seed, datatype):
    if datatype is str:
        buffer.decode()
        return _decryptStr(buffer, seed)
    elif datatype is bytes:
        return _decryptBytes(buffer, seed)

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
