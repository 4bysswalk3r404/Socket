import random
import random

def encrypt(buffer, seed):
    random.seed(seed)
    encrypted = []
    for c in buffer:
        encrypted.append(chr((ord(c) + random.randrange(256)) % 256))
    return ''.join(encrypted).encode()

def decrypt(buffer, seed):
    random.seed(seed)
    encrypted = []
    for c in buffer:
        encrypted.append(chr((ord(c) - random.randrange(256)) % 256))
    return ''.join(encrypted)

if __name__ == "__main__":
    print(decrypt(encrypt('hello world\ntest test', 1), 1))
