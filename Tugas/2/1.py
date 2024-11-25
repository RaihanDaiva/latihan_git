# Fungsi Operator
def input_data():
    global A 
    A = int(input("Masukkan Angka A: "))
    global B
    B = int(input("Masukkan Angka B: "))
def tambah():
    print("\n===Pertambahan===")
    input_data()
    hasil = A + B
    print(f"{A} + {B} = {hasil}")
def kurang():
    print("\n===Pengurangan===")
    input_data()
    hasil = A - B
    print(f"{A} - {B} = {hasil}")
def kali():
    print("\n===Perkalian===")
    input_data()
    hasil = A * B
    print(f"{A} * {B} = {hasil}")
def bagi():
    print("\n===Pembagian===")
    input_data()
    hasil = A / B
    print(f"{A} / {B} = {hasil}")

# Fungsi Menu
def pilih_menu():
    C = int(input("Pilih Salah Satu: "))
    if C == 1:
        tambah()
    elif C == 2:
        kurang()
    if C == 3:
        kali()
    elif C == 4:
        bagi()
def ext():
    while True:
        E = (input("Exit?(y/n)\n"))
        if E == "y":
            exit()
        elif E == "n":
            main()
        else:
            print("(y/n)")
    

# Menu
def main():
    print("\n====Kalkulator Orang Miskin====")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian\n")
 
    pilih_menu()
    ext()
main()
input()