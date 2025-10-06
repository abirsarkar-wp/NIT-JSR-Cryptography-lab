from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Key must be 16, 24, or 32 bytes long
key = b'Sixteen byte key'
data = "This is AES encryption example."

# Encrypt
cipher = AES.new(key, AES.MODE_CBC)
ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
iv = base64.b64encode(cipher.iv).decode('utf-8')
ct = base64.b64encode(ct_bytes).decode('utf-8')

print("---- AES Encryption ----")
print("Original Text:", data)
print("IV:", iv)
print("Cipher Text:", ct)

# Decrypt
iv = base64.b64decode(iv)
ct = base64.b64decode(ct)
cipher = AES.new(key, AES.MODE_CBC, iv)
pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

print("\n---- AES Decryption ----")
print("Decrypted Text:", pt)
