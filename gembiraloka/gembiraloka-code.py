N, M = input().split()
N, M = list(map(int, [N,M]))


total = 0
if(N+M>4):
    if N%4 != 0 and M%4 != 0:
        total += (N%4//2+M%4//2)//2

    total += N//4 + M//4
    print(total)
else:
    print(1)