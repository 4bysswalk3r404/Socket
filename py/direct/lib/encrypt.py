import random

def encrypt(data, seed):
    random.seed(seed)
    return bytes([(b + random.randrange(256)) % 256 for b in data])

def decrypt(data, seed):
    random.seed(seed)
    return bytes([(b - random.randrange(256)) % 256 for b in data])
