kalimat = input()

count = 0
for huruf in kalimat:
    if huruf in ['a', 'i', 'u', 'e', 'o', 'A', 'I', 'U', 'E', 'O']:
        count += 1

count = str(count)
count = ([*count])

if len(count) > 1:
    while len(count) > 1:
        total = sum(list(map(int, count)))
        count = str(total)
    else:
        print(total)
else:
    total = list(map(int, count))
    print(total[0])