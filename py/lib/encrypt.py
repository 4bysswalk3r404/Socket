import random
import caps

def _binaryToDecimal(n):
    return int(n, 2)

def _decimalToBinary(n, bitnum=8):
    return caps.ZeroFill(bin(n).replace("0b",""), bitnum)

#encrypted.append(chr((ord(c) + random.randrange(256)) % 256))
#256 max
def BytesEncode(data):
    encoded = b''
    for c in data:
        encoded += bytes([ord(c)])
    return encoded

def BytesDecode(data):
    decoded = ''
    for b in data:
        decoded += chr(b)
    return decoded

def encrypt(data, seed):
    random.seed(seed)
    encrypted = b''
    for b in data:
        encrypted += chr((ord(b) + random.randrange(256)) % 256)
    return encrypted

def decrypt(data, seed):
    random.seed(seed)
    decrypted = b''
    for b in data:
        decrypted += chr((ord(b) - random.randrange(256)) % 256)
    return decrypted

def charcoal(num, bytelen=3):
    binary = caps.ZeroFill(_decimalToBinary(num), bytelen*8)
    bytevec = caps.Vectorize(binary, 8)
    charred = b''
    for b in bytevec:
        charred += BytesEncode(chr(_binaryToDecimal(b)))
    return charred

def uncharcoal(charred):
    bin = ""
    for c in charred:
        bin += _decimalToBinary(c)
    return _binaryToDecimal(bin)

if __name__ == '__main__':
    num = int(input("num: "))
    charred = charcoal(num)
    print(charred)
    uncharred = uncharcoal(charred)
    print(uncharred)
