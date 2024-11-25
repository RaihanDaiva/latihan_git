def tambah(a, b): #fungsi tambah
    c = a + b   #menyimpan hasil penjumlahan ke var c
    return c    #mengambalikan nilai c
def kurang(a, b):   #fungsi kurang
    c = a - b   ##menyimpan hasil pengurangan ke var c
    return c    #mengambalikan nilai c
def bagi(a, b): #fungsi bagi
    try:    #akan mencoba  
        c = a / b   #proses yang akan dicoba
    except ZeroDivisionError:   #untuk mengatasi error
        print("Tidak bisa dibagi 0")    #mengganti error menjadi string
    else:   #jika except tidak terpenuhi
        print(f"{a} / {b} = {c}")   #maka proses pembagian akan dilaksanakan
def main(): #fungsi utama
    while True: #infinite looping, loop akan berhenti ketika ada perintah seperti break
        print("")   #untuk space
        print("===Pilih Operasi===")    #print judul
        print("1. Penjumlahan") #print pilihan no 1
        print("2. Pengurangan") #print pilihan no 2
        print("3. Perkalian")   #print pilihan no 3
        print("4. Pembagian")   #print pilihan no 4
        print("5. Exit")    #print pilihan no 5
        try:    #akan mencoba
            put = int(input("Pilih (1-5): "))   #yang akan dicoba
        except ValueError:  #untuk mengatasi error
            print("Input Harus Integer!")   #mengganri error menjadi string
            continue    #melanjutkan
        if put < 1 or put > 5:  #jika input diluar dari 1-5, 
            print("Pilihan tidak valid, silakan coba lagi.")    #maka akan menampilkan output tidak valid
            continue    #melanjutkan
        match put:  #untuk menyamakan isi dari variabel put
            case 1: #jika isi dari variabelnya bernilai 1, maka akan menjalankan fungsi tambah
                a = int(input("a: "))   #input a
                b = int(input("b: "))   #input b
                jumlah = tambah(a, b)   #memasukkan hasil penjumlahan ke variabel jumlah
                print(f"{a} + {b} = {jumlah}")  #untuk menampilkan output hasil penjumlahan
            case 2: #jika isi dari variabelnya bernilai 2, maka akan menjalankan fungsi kurang
                a = int(input("a: "))   #input a
                b = int(input("b: "))   #input b
                jumlah = kurang(a, b)   #memasukkan hasil pengurangan ke variabel jumlah
                print(f"{a} - {b} = {jumlah}")  #untuk menampilkan output hasil pengurangan
            case 3: #jika isi dari variabelnya bernilai 3, maka akan menjalankan fungsi kali
                a = int(input("a: "))   #input a
                b = int(input("b: "))   #input b
                kali = lambda a, b: a * b   #fungsi kali dengan menggunakan lambda
                print(f"{a} * {b} = {kali(a, b)}") #menampilkan hasil perkalian
            case 4: #jika isi dari variabelnya bernilai 4, maka akan menjalankan fungsi bagi
                a = int(input("a: "))   #input a
                b = int(input("b: "))   #input b
                bagi(a, b)  #menjalankan fungsi bagi
            case 5: #jika isi dari variabelnya bernilai 5,
                print("Keluar..")   #maka akan menampilkan "keluar"
                break   #untuk keluar dari loop

main()  #menjalankan fungsi main
