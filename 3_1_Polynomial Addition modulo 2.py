def poly_add(a, b):
    return a ^ b

p1 = 0b1011   
p2 = 0b110  

print("P1 =", bin(p1))
print("P2 =", bin(p2))
print("P1 + P2 =", bin(poly_add(p1, p2)))

