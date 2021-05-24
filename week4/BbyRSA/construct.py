#!/usr/bin/env python3
# PyCrypto(!) not PyCryptoDome
from Crypto.PublicKey import RSA

flag = open("flag.txt", "rb").read()
r = RSA.generate(2048, e=7)
c = r.encrypt(flag, "")[0]

ofile = open("output.txt", "w")
print(c.hex(), file=ofile)
print(r.n, file=ofile)
