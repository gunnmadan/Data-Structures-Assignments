def hash(key):
    if isinstance(key, int):
        return key
    elif isinstance(key, float):
        return int(key)
    elif isinstance(key, str):
        polynomial_hash = 0
        for i, char in enumerate(key):
            polynomial_hash += ord(char) * (31 ** (len(key) - 1 - i))
        return polynomial_hash
    elif hasattr(key, '__dict__'):
        address = id(key)
        return hash(str(address))
    else:
        raise ValueError("The provided key is not hashable!")

def compress_division(hash_code, N):
    return hash_code % N

def compress_MAD(hash_code, a, b, p, N):
    return ((a * hash_code + b) % p) % N
