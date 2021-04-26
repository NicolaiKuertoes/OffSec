from Crypto.Cipher import AES
from secret import key, flag, iv
import os

aes = AES.new(key, AES.MODE_CBC, iv)
print(iv.hex() + aes.encrypt(flag).hex())
# Lets not make it that easy
print(key.hex()[:-4])
