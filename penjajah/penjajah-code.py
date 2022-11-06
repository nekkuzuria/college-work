X = input().split()
Y = int(input())

X.sort(reverse=True)

if Y < len(X):
    print(X[Y])
elif Y == len(X):
    print("Semua sudah terjajah")
else:
    print("Maaf negara terlalu kuat")
    