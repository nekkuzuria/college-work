A = input().split()
B = input().split()
C = input().split()
D = input().split()
E = input().split()


A.reverse()
B.reverse()
C.reverse()
D.reverse()
E.reverse()

def ubah_int(x):
    c = int(x[0])
    b = int(x[1])
    a = x[2]
    return (c, b, a)

A = ubah_int(A)
B = ubah_int(B)
C = ubah_int(C)
D = ubah_int(D)
E = ubah_int(E)


lst = [A, B, C, D, E]
lst.sort()

print(lst[2][2].lower())