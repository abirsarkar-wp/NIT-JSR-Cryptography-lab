from Crypto.Cipher import ARC4
import base64

# Key must be between 5 and 256 bytes
key = b"mysecretkey"

# Create cipher object
cipher = ARC4.new(key)

# Plaintext
plaintext = "This is an example of RC4 encryption."
print("Original Text:", plaintext)

# Encrypt
ciphertext = cipher.encrypt(plaintext.encode())
encoded_cipher = base64.b64encode(ciphertext).decode()
print("\nEncrypted (Base64):", encoded_cipher)

# Decrypt
decipher = ARC4.new(key)
decrypted = decipher.decrypt(base64.b64decode(encoded_cipher)).decode()
print("\nDecrypted Text:", decrypted)
