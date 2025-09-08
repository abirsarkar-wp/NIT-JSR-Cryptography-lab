# Polynomial Multiplication over GF(2)
def poly_mul(a, b):
    res = 0
    while b:
        if b & 1:       # if lowest bit of b is 1
            res ^= a    # add (XOR)
        a <<= 1         # shift left = multiply by x
        b >>= 1         # shift right = next coefficient
    return res

# Example
p1 = 0b1011   # x^3 + x + 1
p2 = 0b110    # x^2 + x

print("P1 =", bin(p1))
print("P2 =", bin(p2))
print("P1 * P2 =", bin(poly_mul(p1, p2)))
