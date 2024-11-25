def suhudetak():
    i = 1
    for i in range(3):
        print(f"\n---INPUT {i}---")
        nama = input("Nama: ")
        suhuTubuh = float(input("Suhu Tubuh: "))
        detakJantung = int(input("Detak Jantung: "))
        print(f"\n---OUTPUT {i }---")
        print(f"Nama: {nama}\nSuhu: {suhuTubuh}\nDetak Jantung: {detakJantung}")
        if (suhuTubuh > 39) and (suhuTubuh < 50): 
            print("Harus segera dirawat")
            if detakJantung > 100:
                print("Detak jantung terlalu tinggi, butuh pemeriksaan lebih lanjut.")
            else:
                print("Detak jantung normal, perbanyak istirahat dan minum cairan")
        else:
            print("Cukup istirahat saja") 
            
print("1. Cek Suhu Tubuh dan Detak Jantung")
print("2. Cek Tekanan Darah dan Denyut Nadi")
print("3. None")

def tekanandarah():
    i = 1
    while i < 4 :
        print(f"\n---INPUT {i}---")
        nama = input("Nama: ")
        print("Tekanan Darah:")
        sistolik = int(input(" -Sistolik: "))
        diastolik = int(input(" -Diastolik: "))
        denyut = int(input("Denyut Nadi: "))
        print(f"\n---OUTPUT {i }---")
        print(f"Nama: {nama}\nTekanan Darah:\n -Sistolik: {sistolik}\n -Diastolik: {diastolik}\nDenyut Nadi: {denyut}")
        if sistolik > 180 or diastolik > 120:
            print("Anda mengalami krisis hipertensi, segaralah mencari bantuan medis!!")
        else:
            if sistolik > 140  or diastolik > 90:
                print("kosultasikan dengan dokter mengenai hipertensi")
            elif (sistolik >= 120 and sistolik <= 139) or (diastolik >= 80 and diastolik <= 89):
                print("Anda berada dalam kategori prehipertensi")
            elif sistolik < 120 and diastolik < 80:
                print("Tekanan darah anda normal")
            if denyut > 100:
                print("Periksalah kondisi kesehatabn jantung anda")
            elif denyut < 60:
                print("Periksalah apakah ada gejala lain yang mengiringi bradikardia")
            elif denyut >= 60 and denyut <= 100:
                print("Denyut nadi anda normal")
        i += 1

a = int(input("Pilih Salah Satu: "))
match a:
    case 1:
        suhudetak()
    case 2:
        tekanandarah()
    case 3:
        print("Masih kosong")
    case _:
        print("Input tak valid")

input()

    