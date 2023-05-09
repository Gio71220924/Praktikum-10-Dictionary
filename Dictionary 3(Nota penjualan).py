daftar_barang = {
    'Nama toko' = 'Toko 123',
    'Nama pembeli' = 'Gioo',
    daftar_barang = [
        {'Nomor':1, 'Kode barang': "PO01", 'Nama':"Pensil biasa", 'Harga':1500, 'jml_beli': 2},
        {'Nomor':2, 'kode barang': "P02B", 'Nama':"Pensil 2B", 'Harga': 3500, 'jml_beli': 1},
        {'Nomor':3, 'Kode barang': "Bo01", 'Nama':"Buku", 'Harga': 2500, 'jml_beli': 3},
        {'Nomor':4, 'Kode barang': "Pg01", 'Nama':"Penggaris", 'Harga': 1500, 'jml_beli':4},
        {'Nomor':5, 'Kode barang': "PH01", 'Nama':"Penghapus", 'Harga': 750, 'jml_beli':2},
        {'Nama':"Drawing pen", 'Harga' : 5000, 'jml_beli':2},
    ]
}



#Tampilkan nama toko dan nama pembeli
print(f'Selamat datang di toko {daftar_barang["Nama toko"]} {daftar_barang["Nama pembeli"]}')

#tampilkan daftar barang dan harganya.
for barang in daftar_barang:
    print(f'{barang["Nama"]} - {barang["Harga"]}')

#Tampilkan jumlah barang yang harus dibeli
total_beli = 0


    
    


