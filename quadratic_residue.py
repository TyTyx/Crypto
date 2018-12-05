# Brute force method to determine whether a is QR or QNR mod p.

modulus = 259
a = 9
QR = 0

for b in range(1,int((modulus-1)/2) + 1):
    if (b ** 2) % modulus == a:
        QR = 1

if (QR == 1):
    print (("{} is a QR mod {}").format(a, modulus))
else:
    print (("{} is a QNR mod {}").format(a, modulus))
