def hitung_IMT(weight, height):
    for i in range(1,4):   
        print(f"===Input {i}===")
        weight = float(input("Masukkan Berat Badan Anda(Kg): "))
        height = float(input("Masukkan Tinggi Badan Anda(Meter): "))
        imt = weight / (height**2)
        imt = round(imt, 2)
        print(f"IMT Anda: {imt}")    
        if imt < 18.5:
            print("Kategori Kesehatan Anda: Underweight")
        elif imt < 25:
            print("Kategori Kesehatan Anda: Normal Weight")
        elif imt < 30:
            print("Kategori Kesehatan Anda: Overweight")
        else:
            print("Kategori Kesehatan Anda: Obesity")
        print()
hitung_IMT(0, 0)
input()