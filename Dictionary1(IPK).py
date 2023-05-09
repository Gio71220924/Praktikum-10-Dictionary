data_mahasiswa = {
    "NIM" : '71220924',
    "Nama" : 'Gio',
    "Prodi" :'Informatika',
    "IPK" : 5.2,
    "Semester" : 4,
    "Mata Kuliah":[
        {"nama": "IMK", "SKS" : 3, "Nilai": "B"},
        {"nama":"TekKom", "SKS":3, "Nilai":"A"},
        {"nama":"Jarkom", "SKS":5, "Nilai":"C"},
    ],
}
print(data_mahasiswa['Nama'])
print(f'IPK nya :{data_mahasiswa["IPK"]}')
print(f'Sudah mengambil {len(data_mahasiswa["Mata Kuliah"])} mata kuliah')
transkrip = data_mahasiswa["Mata Kuliah"]
total = 0
for matkul in transkrip:
    if matkul ["Nilai"] == "A":
        print(matkul["nama"])
    total = total + matkul["SKS"]
    
    if matkul["Nilai"] == "A":
        total_bobot = total_bobot + 4*matkul["SKS"]
    elif matkul["Nilai"] == "B":
        total_bobot = total_bobot + 3*matkul["SKS"]
    elif matkul["Nilai"] == "C":
        total_bobot = total_bobot + 2*matkul["SKS"]
    elif matkul["Nilai"] == "D":
        total_bobot = total_bobot + 1*matkul["SKS"]
    elif matkul["Nilai"] == "E":
        total_bobot = total_bobot + 0*matkul["SKS"]

print(f'Total SKS yang sudah diambil:{total} SKS')
ipk = total_bobot/total
data_mahasiswa["IPK"] = ipk
print(data_mahasiswa)