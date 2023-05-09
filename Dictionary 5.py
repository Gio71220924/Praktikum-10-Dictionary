data = dict()
while True:
    angka = int(input("Masukan sebuah angka[negatif untuk berhenti!]:"))
    #jika negatif maka program berhenti?selesai
    if angka < 0:
        break
    #kelompokan angka ganjil dan genap 
    else:
        if angka % 2 == 0:
            if data.get('genap') != None:          #Persiapan di tengah jalan.    
                data["genap"].append(angka)
            else:
                data['genap'] = [angka]
        else:
            if data.get('ganjil') != None:
                data['ganjil'].append(angka)
            else:
                data['ganjil'] = [angka]

print(data)