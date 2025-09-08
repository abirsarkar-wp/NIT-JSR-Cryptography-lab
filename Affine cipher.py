valid_a = [1,3,5,7,9,11,15,17,19,21,23,25]

def modinv(a, m=26):
    for x in range(1, m):
        if (a*x) % m == 1:
            return x
    return None

cipher = "RXQMHSJDGGDRVGHJF"
for a in valid_a:
    a_inv = modinv(a)
    for b in range(26):
        plain = ''.join(chr((a_inv * ((ord(c)-65) - b)) % 26 + 65) if c.isalpha() else c for c in cipher)

        if any(word in plain for word in ("THE","ATTACK","CONFIRM","ME","HERE","DISCOVER","SECRET")):
            print(f"a={a:2d} b={b:2d} -> {plain}")
