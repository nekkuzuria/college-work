# ketika A<B, B-2
# ketika A>B, C+1 
# ketika A=B, nothing to do
# maksimal dua kali istirahat 

a, b, c, i = input().split()
a, b, c, i = list(map(int, [a, b, c, i]))

if a and b and c > 0 and a and b and c < 100:
    if i>0 and i<=2:
        for x in range (i):
            if a<b :
                a = a + 2 
                b = b - 2
            elif a>b :
                a = a - 1  
                c = c + 1 

print(a, b, c)

