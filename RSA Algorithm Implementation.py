import random
from math import gcd

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def get_prime(start=100, end=300):
    while True:
        p = random.randint(start, end)
        if is_prime(p): return p


def modinv(a, m):
    def egcd(a, b):
        if b == 0: return (a, 1, 0)
        g, x, y = egcd(b, a % b)
        return (g, y, x - (a // b) * y)
    g, x, _ = egcd(a, m)
    if g != 1: raise Exception('No modular inverse')
    return x % m


def generate_keys():
    p, q = get_prime(), get_prime()
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = modinv(e, phi)
    return (n, e), (n, d)


def encrypt(msg, pub):
    n, e = pub
    return [pow(ord(ch), e, n) for ch in msg]

def decrypt(cipher, priv):
    n, d = priv
    return ''.join(chr(pow(c, d, n)) for c in cipher)


if __name__ == "__main__":
    pub, priv = generate_keys()
    print("Public key:", pub)
    print("Private key:", priv)

    text = "HELLO RSA"
    print("\nOriginal:", text)

    enc = encrypt(text, pub)
    print("Encrypted:", enc)

    dec = decrypt(enc, priv)
    print("Decrypted:", dec)
