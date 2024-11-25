def celcius():  #untuk membuat fungsi mengkonversi suhu celcius ke suhu lainnya
    print("===CELCIUS===")
    c = int(input("Masukkan suhu(Celcius): "))  #untuk menginput suhu celcius yang ingin di konversi
    k = c + 273.15  #proses mengkonversikan celcius ke kelvin
    print(f"a. Kelvin: {k} K")  #menampilkan output konversi celcius ke kelvin
    f = (9/5) * c + 32  #proses mengkonversikan celcius ke farenheit
    print(f"b. Farenheit: {f} °F")  #menampilkan output konversi celcius ke farenheit
    r = (4/5) * c   #proses mengkonversikan celcius ke reamur
    print(f"c. Reamur: {r} °R") #menampilkan output konversi celcius ke reamur
    
def farenheit():    #untuk membuat fungsi mengkonversi suhu farenheit ke suhu lainnya
    print("===FARENHEIT===")
    f = int(input("Masukkan suhu(Farenheit): "))    #untuk menginput suhu farenheit yang ingin di konversi
    k =  (f + 459.67) * 5/9 #proses mengkonversikan farenheit ke kelvin
    k = round(k, 2) #agar formatnya menjadi format rupiah
    print(f"a. Kelvin: {k} K")  #menampilkan output konversi farenheit ke kelvin
    r = 4/9 * (f-32)    #proses mengkonversikan farenheit ke reamur
    r = round(r, 2)     #agar formatnya menjadi format rupiah
    print(f"b. Reamur: {r} °R") #menampilkan output konversi farenheit ke reamur
    c = (f - 32) * 5/9  #proses mengkonversikan farenheit ke celcius
    c = round(c, 2)     #agar formatnya menjadi format rupiah
    print(f"c. Celcius: {c} °C")    #menampilkan output konversi farenheit ke celcius
    
def reamur():   #untuk membuat fungsi mengkonversi suhu reamur ke suhu lainnya
    print("===REAMUR===")
    r = int(input("Masukkan suhu(Reamur): "))   #untuk menginput suhu reamur yang ingin di konversi
    f = (r * 2.25) + 32 #proses mengkonversikan reamur ke farenheit
    print(f"a. Farenheit: {f} °F")  #menampilkan output konversi reamur ke farenheit
    c = r / 0.8 #proses mengkonversikan reamur ke celcius
    print(f"b. Celcius: {c} °C")    #menampilkan output konversi reamur ke celcius
    k = (r / 0.8) + 273.15  #proses mengkonversikan reamur ke kelvin
    print(f"c. Kelvin: {k} K")  #menampilkan output konversi reamur ke kelvin
    
def kelvin():   #untuk membuat fungsi mengkonversi suhu kelvin ke suhu lainnya
    print("===KELVIN===")
    k = int(input("Masukkan suhu(Kelvin): "))   #untuk menginput suhu kelvin yang ingin di konversi
    c = k - 273.15  #proses mengkonversikan kelvin ke celcius
    c = round(c, 2) #agar formatnya menjadi format rupiah
    print(f"a. Ceclius: {c} °C")     #menampilkan output konversi kelvin ke celcius
    f = (k * 9/5) - 459.67  #proses mengkonversikan kelvin ke farenheit
    print(f"b. Farenheit: {f} °F")   #menampilkan output konversi kelvin ke farenheit
    r = 4/5 *(k - 273)  #proses mengkonversikan kelvin ke reamur
    print(f"c. Reamur: {r} °R") #menampilkan output konversi kelvin ke reamur

def main():     #untuk membuat fungsi utama
    put = int(input("Pilih Salah Satu Yang Ingin Di Konversi: "))   #untuk memilih suhu mana yang ingin dikonversikan
    print()
    match put:  #input dari variabel put akan di match dengan case-case yang telah disediakan
        case 1:
            celcius()   #jika inputnya 1, maka akan menjalankan fungsi celcius()
        case 2:
            farenheit() #jika inputnya 2, maka akan menjalankan fungsi farenheit()
        case 3:
            reamur()    #jika inputnya 3, maka akan menjalankan fungsi reamur()
        case 4:
            kelvin()    #jika inputnya 4, maka akan menjalankan fungsi kelvin()
        case _: #jika input putnya bukan 1-4 maka akan mengeluarkan output 'input tidak valid', dan akaan disuruh menginput ulang
            print("Input tidak valid")
            main()  #untuk menjalankan fungsi main(), agar user bisa menginput ulang
print("===KONVERSI SUHU===")
print("1. Celcius")
print("2. Farenheit")
print("3. Reamur")
print("4. Kelvin")
main()  #untuk menjalankan fungsi main()
input() #agar program tidak langsung keluar