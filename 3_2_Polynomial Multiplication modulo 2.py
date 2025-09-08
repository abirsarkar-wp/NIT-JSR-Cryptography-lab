def poly_mul(a, b):
    res = 0
    while b:
        if b & 1:       
            res ^= a
        a <<= 1         
        b >>= 1         
    return res


p1 = 0b1011   
p2 = 0b110    

print("P1 =", bin(p1))
print("P2 =", bin(p2))
print("P1 * P2 =", bin(poly_mul(p1, p2)))

