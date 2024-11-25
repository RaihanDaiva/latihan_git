angka = [] #mendeklarasikan variabel sebagai list kosong 
a = 10   #mendeklarasaikan varibel a dengan nilainya 10
for i in range(a):  #batas loop ini adalah sampai nilai dari varibel a
    put = int(input(f"Masukkan angka ke-{i+1}: "))  #untuk input angka
    angka.append(put)   #isi dari inputan tersebut akan dimasukkan kedalam list angka

print(angka)    #untuk menampilkan isi dari list angka
print("===No 1===")    
mn = min(angka) #mengisi variabel mn dengan nilai paling kecil dari angka yang ada di dalam list angka 
mx = max(angka) #mengisi variabel mx dengan nilai paling besar dari angka yang ada di dalam list angka 
avg = sum(angka) / a    #menghitung rata-rata dari semua angka yang ada di dalam list angka
avg = round(avg, 2) #untuk membulatkan angka pada nilai variabel avg hingga 2 angka desimal
print(f"Angka Terendah: {mn}")  #menampilkan angka terendah
print(f"Angka Tertinggi: {mx}") #menampilkan angka tertinggi
print(f"Rata-rata: {avg}")  #menampilkan rata-rata
print("===No 2===")
jmlh = sum(angka)   #menjumlahkan semua isi angka yang ada di dalam list angka
j_genap = 0 #mendeklarasikan variabel j_genap agar bernilai 0
j_ganjil = 0    #mendeklarasikan variabel j_ganjil agar bernilai 0
print(f"Jumlah: {jmlh}")    #menampilkan jumlah
for i in (angka):   #batas loop ini adalah sampai maksimal index yang ada pada list angka
    if i % 2 == 1:  #kita misalkan ini adalah loop pertama, maka nilai i pada loop pertama adalah angka dari index pertama pada list angka
        j_ganjil += 1   #jadi jika nilai index pertama dibagi 2 itu hasil baginya menyisakan 1, maka variabel j_ganjil akan ditambahkan 1
    else:   #kecuali jika hasil baginya menyisakan selain satu, maka variabel j_genap akan ditambahkan 1
        j_genap += 1 
print(f"Jumlah Bil Ganjil: {j_ganjil}") #menampilkan jumlah bilangan ganjil
print(f"Jumlah Bil Genap: {j_genap}")   #menampilkan jumlah bilangan genap
print("===No 3===")
angka.sort(reverse=True)    #untuk mengurutkan angka dari yang terbesar ke terkecil pada list  
print(angka)    #menaampilkan urutan angka dari yang terbesar ke yang terkecil
print("===No 4===")
for i in (angka):   #batas loop ini adalah sampai maksimal index yang ada pada list angka
    if i < 0:   #pada loop ini akan mengecek semua angka yang ada pada list angka, jika pada list terdapat angka negatif. maka akan menampilkan "ada angka negatif"
        print("Ada angka negatif")  
        break  #jika if terpenuhi maka break dijalankan, yang berarti loop akan diberhentikan walaupun loopnya belum selesai
else:   #else disini adalah else untuk loop, else ini akan dijalankan jika dan hanya jika loop selesai tanpa diberhentikan menggunakan break
    print("Tidak ada angka negatif")    #lalu jika loop selesai tanpa di break, maka akan menampilkan output "Tidak ada angka negatif"
    
input()