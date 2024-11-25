# Fungsi untuk konversi suhu
def celsius_to_kelvin(c):
    return c + 273

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_reamur(c):
    return c * 4/5

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273

def fahrenheit_to_reamur(f):
    return fahrenheit_to_celsius(f) * 4/5

def reamur_to_celsius(r):
    return r * 5/4

def reamur_to_fahrenheit(r):
    return (reamur_to_celsius(r) * 9/5) + 32

def reamur_to_kelvin(r):
    return reamur_to_celsius(r) + 273

def kelvin_to_celsius(k):
    return k - 273

def kelvin_to_fahrenheit(k):
    return (kelvin_to_celsius(k) * 9/5) + 32

def kelvin_to_reamur(k):
    return kelvin_to_celsius(k) * 4/5

# Program utama untuk memilih dan melakukan konversi
def main():
    print("Program Konversi Suhu")
    print("Pilih jenis konversi:")
    print("a. Celsius")
    print("b. Fahrenheit")
    print("c. Reamur")
    print("d. Kelvin")
    
    choice = input("Masukkan pilihan (a/b/c/d): ").lower()
    
    if choice == 'a':
        c = float(input("Masukkan suhu dalam Celsius: "))
        print(f"Celsius ke Kelvin: {celsius_to_kelvin(c)} K")
        print(f"Celsius ke Fahrenheit: {celsius_to_fahrenheit(c)} °F")
        print(f"Celsius ke Reamur: {celsius_to_reamur(c)} °R")
        
    elif choice == 'b':
        f = float(input("Masukkan suhu dalam Fahrenheit: "))
        print(f"Fahrenheit ke Celsius: {fahrenheit_to_celsius(f)} °C")
        print(f"Fahrenheit ke Kelvin: {fahrenheit_to_kelvin(f)} K")
        print(f"Fahrenheit ke Reamur: {fahrenheit_to_reamur(f)} °R")
        
    elif choice == 'c':
        r = float(input("Masukkan suhu dalam Reamur: "))
        print(f"Reamur ke Celsius: {reamur_to_celsius(r)} °C")
        print(f"Reamur ke Fahrenheit: {reamur_to_fahrenheit(r)} °F")
        print(f"Reamur ke Kelvin: {reamur_to_kelvin(r)} K")
        
    elif choice == 'd':
        k = float(input("Masukkan suhu dalam Kelvin: "))
        print(f"Kelvin ke Celsius: {kelvin_to_celsius(k)} °C")
        print(f"Kelvin ke Fahrenheit: {kelvin_to_fahrenheit(k)} °F")
        print(f"Kelvin ke Reamur: {kelvin_to_reamur(k)} °R")
        
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
