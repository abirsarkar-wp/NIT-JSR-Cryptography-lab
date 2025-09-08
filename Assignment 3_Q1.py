# Polynomial Addition over GF(2)
def poly_add(a, b):
    return a ^ b   # XOR is addition in GF(2)

# Example
p1 = 0b1011   # x^3 + x + 1
p2 = 0b110    # x^2 + x

print("P1 =", bin(p1))
print("P2 =", bin(p2))
print("P1 + P2 =", bin(poly_add(p1, p2)))
