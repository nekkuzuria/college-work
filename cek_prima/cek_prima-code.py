angka = int(input())

prima = True
i = 2
while i**2 <= angka:
    if angka%i==0:
        prima = False
    i += 1

if prima==True:
    print("PRIMA")
else:
    print("BUKAN PRIMA")

