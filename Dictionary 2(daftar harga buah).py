daftar_harga = [
    {'Nama': 'Apel', 'Harga':10000},
    {'Nama':'Jeruk', 'Harga' : 20000},
    {'Nama':'Durian', 'Harga' : 120000},
    {'Nama':'Kiwi', 'Harga' : 60000},
    {'Nama':'Melon', 'Harga' : 300000},
]

#Tampilkan semua buah dan harganya
for buah in daftar_harga:
    print(f'{buah["Nama"]} - {buah["Harga"]}')

#Tampilkan nama buah yang harganya paling mahal
mahal = 0
buah_mahal = ''
for buah in daftar_harga:
    if buah['Harga'] > mahal:
        mahal = buah['Harga']
        buah_mahal = buah['Nama']

print(f'Nama buah termahal adalah {buah_mahal} dengan harga {mahal}')

#Hapus buah yang harganya < 100 ribu.
batas = 100000

#Ambil dulu jumlah dalam list
count = len (daftar_harga)
index = 0
while index < count:
    if daftar_harga[index]['Harga'] < batas:
        #harus dihapus
        del daftar_harga['index']
    else:
        index = index + 1
    count = len(daftar_harga)


#Tampilkan semua buah dan harganya
print("Setelah semua buah di bawah batas harga dihapus")
for buah in daftar_harga:
    print(f'{buah["Nama"]} - {buah["Harga"]}')

    