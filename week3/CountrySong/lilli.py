import Cryptodome as Crypto
from Cryptodome.Cipher import AES
import time
startTime = time.perf_counter()
#hier pfad eingeben wo die Dateien liegen
pathInput = "./"




#given
#keys (missing 3 bytes (6 hextetts) each)
key1 = bytes.fromhex('45af2ea847cd99b17e76e6a1d1')
missing1=bytes.fromhex('00 00 00')
key2 = bytes.fromhex('80642d611a08d0d1e091f8476b')
missing2 = bytes.fromhex('00 00 00')

#encrypted msg
f = open('output.txt', 'r')
givenOutputEnc = f.readline()[:-1]
#encrypted flag only
flagEnc = bytes.fromhex(givenOutputEnc[32:])
#für vergleiche reichen aber erste 16 byte wegen png:
PNGDoubleEnc = bytes.fromhex(givenOutputEnc[32:64])
#iv given
iv = bytes.fromhex(givenOutputEnc[:32])
mode = AES.MODE_CBC
#we know, we are looking for a png-file
#normaler PNG-Start inklusive IHDR.
pngPlain = bytes.fromhex('89 50 4e 47 0d 0a 1a 0a 00 00 00 0d 49 48 44 52')


def decryptFile(key1, key2, iv, flagEnc, destination):
    cipher1 = AES.new(key1, AES.MODE_CBC, iv)
    cipher2 = AES.new(key2, AES.MODE_CBC, iv)

    with open(destination, 'wb') as f:
        f.write(cipher1.decrypt(cipher2.decrypt(flagEnc)))



print("Starting inner encryption")
dict={}
missingBytes=[0x0,0x0,0x0]
keyComb = key2+missing2
for i in range(256):
    missingBytes[1] = 0x0
    for j in range(256):
        missingBytes[2]=0x0
        for k in range(256):
            keyComb = key2+bytes(missingBytes.copy())
            cipher2 = AES.new(keyComb, AES.MODE_CBC, iv)
            pngEnc = cipher2.encrypt(pngPlain)
            dict[pngEnc]= keyComb
            missingBytes[2] +=1
        missingBytes[1] +=1
    missingBytes[0] += 1




#2. runde. Das hier könnte man auch super parallelisieren um schneller zu sein.

print("Starting outer decryption")
zaehler = 0
missingBytes=[0x0,0x0,0x0]
keyComb = key1+missing1
for i in range(256):
    missingBytes[1] = 0x0
    for j in range(256):
        missingBytes[2]=0x0
        for k in range(256):
            keyComb = key1+bytes(missingBytes.copy())
            cipher1 = AES.new(keyComb, AES.MODE_CBC, iv)
            zaehler +=1
            test = cipher1.decrypt(PNGDoubleEnc)
            if (test in dict):
                print("Schlüssel gefunden (1,2):")

                print(dict[test].hex(), keyComb.hex())
                decryptFile( keyComb, dict[test], iv, flagEnc, 'flaggyMCflagface.png')
                break
            missingBytes[2] +=1
        missingBytes[1] +=1
    missingBytes[0] += 1

endTime = time.perf_counter()
print('\nDauer: \t ', endTime-startTime)
