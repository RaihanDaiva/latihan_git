jpasien = int(input("Masukkan Jumlah Pasien: "))
nama = []
suhu = []

for i in range (jpasien):
    nama_pasien = input(f"Masukkan Nama Pasien: ")
    nama.append(nama_pasien)
    suhu_pasien = float(input(f"Masukkan Suhu Pasien:"))
    suhu.append(suhu_pasien)
    # print(nama,suhu)
    
total_suhu = 0
for i in range (jpasien):
    total_suhu = suhu[i] + total_suhu
    if suhu[i] > 45:
        print(f"nama yang diambang batas: {nama[i]}")

avg = total_suhu / jpasien

print(f"Rata-rata = {avg}")
    
    
