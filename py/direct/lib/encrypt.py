import random
import caps

def _binaryToDecimal(n):
    return int(n, 2)

def _decimalToBinary(n, bitnum=8):
    return caps.ZeroFill(bin(n).replace("0b",""), bitnum)

def BytesEncode(string):
    return bytes([ord(c) for c in string])

def BytesDecode(data):
    return ''.join([chr(b) for b in data])

def encrypt(data, seed):
    random.seed(seed)
    return bytes([(b + random.randrange(256)) % 256 for b in data])

def decrypt(data, seed):
    random.seed(seed)
    return bytes([(b - random.randrange(256)) % 256 for b in data])

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
