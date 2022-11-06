j = int(input())
m = int(input())

menit = [10, 15, 20, 30]
wakt_tempuh = [40, 30, 20, 10]
jam = [j, j, j, j]
tarif = [5000, 10000, 13000, 17000]
total_ongkos = [100000, 100000, 100000, 100000]
warna = ["Biru", "Merah", "Hijau", "Putih"]

for a in range(4):
    if m%menit[a]==0:
        menit[a] = m
    else:
        menit[a] = m // menit[a] * menit[a] + menit[a] #menit keberangkatan
        
    menit[a] += wakt_tempuh[a] #menit smpai
    
    if menit[a]>=60: #klo lebih dr 60, jamnya tambah 1
        jam[a] += 1
        menit[a] -= 60
    
    total_ongkos[a] += tarif[a] #pakan + tarif angkot
    
    if jam[a]==8:
        if menit[a] < 15:
            total_ongkos[a] += 10000 #total ongkos klo lebih dr jm 8
        else:
            total_ongkos[a] += (menit[a]//15 + 1)*10000 #total ongkos klo lebih dr jm 8
    elif jam[a] == 9:
        if menit[a] < 15:
            total_ongkos[a] += 10000*5 #total ongkos klo lebih dr jm 9
        else:
            total_ongkos[a] += (menit[a]//15+1)*10000 + 10000*4
    

print(warna[total_ongkos.index(min(total_ongkos))])
    

