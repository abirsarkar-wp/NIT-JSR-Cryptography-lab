# Simplified Triple DES (3DES) Implementation without using crypto library

def xor(a, b): return ''.join('0' if i == j else '1' for i, j in zip(a, b))

# Simple permutation function (for demo)
def permute(block, table): return ''.join(block[i - 1] for i in table)

# Simple round function (not full DES, just mimics behavior)
def f(right, key):
    return xor(right, key[:len(right)])[::-1]  # reverse for mixing

# Simplified DES with 4 rounds
def des_encrypt(text, key):
    left, right = text[:len(text)//2], text[len(text)//2:]
    for _ in range(4):
        left, right = right, xor(left, f(right, key))
    return right + left

def des_decrypt(text, key):
    left, right = text[:len(text)//2], text[len(text)//2:]
    for _ in range(4):
        left, right = right, xor(left, f(right, key))
    return right + left

# Triple DES
def triple_des_encrypt(pt, k1, k2, k3):
    return des_encrypt(des_decrypt(des_encrypt(pt, k1), k2), k3)

def triple_des_decrypt(ct, k1, k2, k3):
    return des_decrypt(des_encrypt(des_decrypt(ct, k3), k2), k1)

# Example binary data
plaintext = '1010101111001101111011110001001100110011010101011111000010101010'
k1 = '1100110011001100110011001100110011001100110011001100110011001100'
k2 = '1111000011110000111100001111000011110000111100001111000011110000'
k3 = '0000111100001111000011110000111100001111000011110000111100001111'

print("Plaintext :", plaintext)
cipher = triple_des_encrypt(plaintext, k1, k2, k3)
print("Ciphertext:", cipher)
decrypted = triple_des_decrypt(cipher, k1, k2, k3)
print("Decrypted :", decrypted)
