def caesar_decrypt(ct, k):
    return ''.join(chr((ord(c)-65 - k) % 26 + 65) if c.isalpha() else c for c in ct)

cipher = "UDUCOYIQFFHEQSXYD"
for k in range(26):
    print(f"Key={k:2d} -> {caesar_decrypt(cipher, k)}")
