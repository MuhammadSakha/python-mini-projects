print ('Menu Pesanan')
print ('1. Burger : 25.000')
print ('2. Kentang Goreng : Rp15.000')
print ('3. Minuman : Rp10.000 ')
print ('0. selesai memesan')

total = 0
pesanan = []
selesai = 0 #Penanda agar loop berhenti jika user pilih 0

#perulangan untuk memilih menu
while selesai == 0:
    pilihan = int(input('\n pilih menu (1-3) atau 0 untuk selesai: '))

    if pilihan == 1:
        pesanan.append('burger')
        total += 25000
    elif pilihan == 2:
        pesanan.append('Kentang Goreng')
        total += 15000
    elif pilihan == 3:
        pesanan.append('minuman')
        total += 10000
    elif pilihan == 0:
        selesai = 1
    else:
        print('Pilihan tidak tersedia,coba lagi')

if total > 60000:
    diskon = total*0.3
else:
    diskon = 0

total_bayar = total - diskon
    
#Tampilkan hasil akhir
print('\n=== Rincian Pesanan===')
for i in range(len(pesanan)):
    print(f'{i+1}.{pesanan[i]}')
    
print('Total sebelum diskon :', total)
print('Jumlah diskon : ', int(diskon))
print('Total yang harus dibayar : ', int(total_bayar))
print('Jumlah pesanan : ', pesanan)

    
    

        
