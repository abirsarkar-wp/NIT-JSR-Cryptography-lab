valid_keys = [1,3,5,7,9,11,15,17,19,21,23,25]

def modinv(a, m=26):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    return None

cipher = "TQKECDIVYIBIVI"
for a in valid_keys:
    inv = modinv(a)
    plain = ''.join(chr((inv * (ord(c)-65)) % 26 + 65) if c.isalpha() else c for c in cipher)
    print(f"Key a={a:2d} (inv={inv:2d}) -> {plain}")
