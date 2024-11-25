# Soal
# Anda bekerja sebagai pengembang perangkat lunak di sebuah klinik kesehatan yang ingin membuat aplikasi sederhana untuk mencatat data pasien dan menganalisis tekanan darah. Tugas Anda adalah membuat program yang dapat melakukan hal berikut:
# 1. Meminta pengguna untuk memasukkan jumlah pasien yang akan didaftarkan.
# 2. Untuk setiap pasien, minta pengguna memasukkan nama, tekanan darah sistolik, dan tekanan darah diastolik.
# 3. Simpan data setiap pasien dalam tiga list terpisah, satu untuk nama, satu untuk tekanan darah sistolik, dan satu untuk tekanan darah diastolik.
# 4. Hitung dan tampilkan rata-rata tekanan darah sistolik dan diastolik dari semua pasien.
# 5. Tampilkan nama-nama pasien yang memiliki tekanan darah sistolik di atas 140 atau tekanan darah diastolik di atas 90, yang menandakan hipertensi.

# Jawaban :

nama = [] #variabek untuk menyimpan list kosong
sistolik = []   #variabek untuk menyimpan list kosong
diastolik = []  #variabek untuk menyimpan list kosong

jpasien = int(input("Masukkan jumlah pasien yang akan didaftarkan: "))  #untuk menginput jumlah pasien yang ingin di daftarkan

for i in range (jpasien):   #for loop dengan batasnya adalah inputan dari variabel 'jpasien'
    print(f"Pasien ke-{i+1}")   #untuk menanda pasien yang sedang diinput itu pasien ke berapa
    nama_pasien = input("Masukkan Nama Pasien: ")   #untuk menginput nama pasien
    nama.append(nama_pasien)    #memasukkan inputan 'nama_pasien' kedalam list 'nama'
    sistolik_pasien = int(input("Masukkan darah sistolik pasien: "))    ##untuk menginput sistolik pasien
    sistolik.append(sistolik_pasien)    #memasukkan inputan 'sistolik_pasien' kedalam list 'sistolik'
    diastolik_pasien = int(input("Masukkan darah diastolik pasien: "))  ##untuk menginput diastolik pasien
    diastolik.append(diastolik_pasien)  #memasukkan inputan 'diastolik_pasien' kedalam list 'diastolik'
    
avg_s = sum(sistolik) / jpasien #proses menghitung rata-rata sistolik dengan cara menjumlahkan terlebih dahulu isi dari list 'sistolik', lalu dibagi dengan jumlah pasien
avg_s = round(avg_s, 2) ##untuk membulatkan angka pada nilai variabel avg_s hingga 2 angka desimal
avg_d = sum(diastolik) / jpasien    #proses menghitung rata-rata diastolik dengan cara menjumlahkan terlebih dahulu isi dari list 'diastolik', lalu dibagi dengan jumlah pasien
avg_d = round(avg_d, 2) #untuk membulatkan angka pada nilai variabel avg_d hingga 2 angka desimal

print() #agar memiliki space untuk input dan output

print(f"Rata-rata Sistolik Pasien: {avg_s}")    #menampilkan output dari rata-rata sistolik semua pasien
print(f"Rata-rata Diastolik Pasien: {avg_d}")   #menampilkan output dari rata-rata diastolik semua pasien

for i in range(jpasien):    #for loop dengan batasnya adalah inputan dari variabel 'jpasien'
    if sistolik[i] > 140 or diastolik[i] > 90:  #untuk kondisional, jadi nilai i yang diloop akan mencek tiap index di dalam list 'sistolik' dan 'diastolik'. lalu untuk kondisionalnya jika sistolik > 140 atau diastolik > 90, maka akan menampilkan pasien yang mengalami hipertensi   
        print(f"Nama pasien yang mengalami hipertensi: {nama[i]}")  #jadi nilai i yang diloop akan mencek tiap index di dalam list 'nama', dan akan menampilkan nama yang yang mengalami hipertensi

input() #untuk input, tetapi fungsinya agar programnya tidak langsung keluar