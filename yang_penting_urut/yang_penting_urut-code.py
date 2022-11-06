s = input()
s = list(map(ord, s))
mid = len(s)//2


if len(s)%2==0:
    print("TIDAK TERURUT")
else:
    if s[len(s)-1]-s[0]==2 and s[mid]-s[0]==1:
      print("TERURUT")
    else:
      print("TIDAK TERURUT")