def suhudetak():
    for i in range(3):
        nama = input("Nama: ")
        suhuTubuh = float(input("Suhu Tubuh: "))
        detakJantung = int(input("Detak Jantung: "))

        print(f"Nama: {nama}\nSuhu: {suhuTubuh}\nDetak Jantung: {detakJantung}\n")
        if (suhuTubuh > 39) and (suhuTubuh < 50): 
            print("Harus segera dirawat")
            if detakJantung > 100:
                print("Detak jantung terlalu tinggi, butuh pemeriksaan lebih lanjut.")
            else:
                print("Detak jantung normal, perbanyak istirahat dan minum cairan")
        else:
            print("Cukup istirahat saja") 
            
print("1. Cek Suhu Tubuh dan Detak Jantung")
print("2. None")
print("3. None")

a = int(input("Pilih Salah Satu: "))

match a:
    case 1:
        suhudetak()
    case 2:
        print("Masih kosong")
    case 3:
        print("Masih kosong")
    case _:
        print("Input tak valid")

input()