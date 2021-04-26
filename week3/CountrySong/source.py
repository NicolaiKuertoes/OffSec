from Crypto.Cipher import AES
from Crypto.Util import Padding
from secret import key1, key2, iv
import os

# Flag is in this image
flag = open("flag.png", "rb").read()
# Pad to 16 byte block length
flag = Padding.pad(flag, 16)

aes1 = AES.new(key1, AES.MODE_CBC, iv)
aes2 = AES.new(key2, AES.MODE_CBC, iv)

with open("output.txt", "w") as f:
    f.write(iv.hex() + aes1.encrypt(aes2.encrypt(flag)).hex() + "\n")
    # This time, three bytes are missing <@:-E
    f.write(key1.hex()[:-6] + "\n")
    f.write(key2.hex()[:-6] + "\n")
