def poly_mul_mod(a, b, mod):
    res = 0
    while b:
        if b & 1:
            res ^= a
        a <<= 1
        
        if a & (1 << (mod.bit_length() - 1)):
            a ^= mod
        b >>= 1
    return res


mod = 0b100011011
p1 = 0b1011   
p2 = 0b110    

print("P1 =", bin(p1))
print("P2 =", bin(p2))
print("Modulo Polynomial =", bin(mod))
print("P1 * P2 mod mod =", bin(poly_mul_mod(p1, p2, mod)))

