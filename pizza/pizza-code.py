a = input()
b = input()
c = input()

a = int(a[0])/int(a[2])
b = int(b[0])/int(b[2])
c = int(c[0])/int(c[2])

pizza = 0
if a+b > 1 :
    pizza += 2
    if b+c > 1:
        pizza +=1
else:
    pizza += 1
    if a+b+c > 1 :
        pizza += 1

print(pizza+1)
    
    
        
    

