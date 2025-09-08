# Efficient Multiplication modulo irreducible polynomial (AES style)
def poly_mul_mod(a, b, mod):
    res = 0
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        # If degree >= mod degree, reduce
        if a & (1 << (mod.bit_length() - 1)):
            a ^= mod
        b >>= 1
    return res

# Example with AES irreducible polynomial (x^8 + x^4 + x^3 + x + 1)
mod = 0b100011011
p1 = 0b1011   # x^3 + x + 1
p2 = 0b110    # x^2 + x

print("P1 =", bin(p1))
print("P2 =", bin(p2))
print("Modulo Polynomial =", bin(mod))
print("P1 * P2 mod mod =", bin(poly_mul_mod(p1, p2, mod)))
