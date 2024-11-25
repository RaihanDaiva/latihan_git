
a = [50000, 75000, 100000]  #Mendeklarasikan variabel a sebagai list yang memiliki 3 nilai
def main(): #untuk membuat fungsi utama
    put = int(input("Pilih Film: "))    #untuk menginput film yang dipilih
    qty = int(input("Jumlah Tiket: "))  #untuk menginput jumlah tiket yang diinginkan
    match put:  #input dari variabel put akan di match dengan case-case yang telah disediakan
        case 1:
            pilihan = a[0]  #jika input putnya adalah 1 maka isi varibel pilihan = a[0]/50000
        case 2:
            pilihan = a[1]  #jika input putnya adalah 2 maka isi varibel pilihan = a[1]/75000
        case 3:
            pilihan = a[2]  #jika input putnya adalah 3 maka isi varibel pilihan = a[2]/100000
        case _: #jika input putnya bukan 1-3 maka akan mengeluarkan output 'input tidak valid', dan akaan disuruh menginput ulang
            print("Input Tidak Valid")
            main()  #untuk menjalankan fungsi main(), agar user bisa menginput ulang    
    harga = pilihan * qty   #variabel a = pilihan * qty
    total = harga   #variabel total = harga
    h_awal = pilihan * qty  #variabel h_awal = pilihan * qty
    vip = input("Apakah Anda VIP?(y/n): ")  #untuk menginput apakah user adalah member VIP atau bukan
    print()
    print(f"Harga Awal: {h_awal:,.0f}".replace(",", "."))   #untuk menampilkan harga awal
    if vip == "y":  #jika user adalah member VIP, maka akan mendapatkan diskon 20%
        diskon_vip = harga * 0.2
        total -= diskon_vip
        print("Diskon VIP: 20%")
    if qty > 5: #jika user membeli tiket lebih dari 5, maka akan mendapatkan diskon sebesar 10%
        diskon_qty = harga * 0.1
        total -= diskon_qty
        print("Diskon Beli > 5 Tiket: 10%")
    else:   #jika tidak keduanya, maka tidak mendapatkan diskon sama sekali
        return  #untuk keluar dari fungsi 'if'
    print(f"Total: Rp {total:,.0f}".replace(",", "."))  #untuk menampilkan harga totalnya
            
print("===TIKET BIOSKOP===")
print("1. Film A: Rp 50.000")
print("2. Film B: Rp 75.000")
print("3. Film C: Rp 100.000")
main()  #untuk memanggil fungsi main()
input() #agar program tidak langsung keluar