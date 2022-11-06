# input
X, Y = input().split()
XX, YY = input().split()
X, Y, XX, YY = list(map(int, [X,Y, XX, YY]))


print("-"*X) #batas atassss
# =======================================
sebaris= "*"*X + '\n'
peta = sebaris*Y

indeks = (X+1)*(YY-1) + XX

peta = peta[:indeks-1] + "=" + peta[indeks:]
print(peta, end="")
# ==============================================
print("-"*X) #batas bawah



