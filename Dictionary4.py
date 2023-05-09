#persiapan dari awal
data = {"Genap":[], 'Ganjil':[]}
while True:
    angka = int(input("Masukan sebuah angka[negatif untuk berhenti!]:"))
    #jika negatif maka program berhenti?selesai
    if angka < 0:
        break
    #kelompokan angka ganjil dan genap 
    else:
        if angka % 2 == 0:              
            data["Genap"].append(angka)
        else:
            data['Ganjil'].append(angka)
print(data)