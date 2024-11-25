# while True:
#     gender = input("Gender(L/P): ")
#     if gender != "L" and gender != "P":
#         print("Input tidak valid")
#     else:
#         while True:
#             try:
#                 usia = int(input("Usia anda: "))
#                 if usia == int:
#                     if (usia >= 3) and (usia <= 18):
#                         if gender == "L" :
#                             print("Minumlah air sebanyak 1.6 liter")
#                         elif gender == "P":
#                             print("Minumlah air sebanyak 1.4 liter")
#                     elif (usia >= 18) and (usia <= 64):
#                         if gender == "L" :
#                             print("Minumlah air sebanyak 2.5 liter")
#                         elif gender == "P":
#                             print("Minumlah air sebanyak 2.0 liter")
#                     elif (usia >= 65):
#                         if gender == "L" :
#                             print("Minumlah air sebanyak 2.0 liter")
#                         elif gender == "P":
#                             print("Minumlah air sebanyak 1.8 liter")
#                     else:
#                             print("Masih diberi ASI")
#                     break
#             except ValueError:
#                 print("Input tidak valid")
# input()
while True:
    try:
        usia = int(input("Usia: "))
        gender = int (input("Masukkan angka 1 untuk Laki-laki dan angka 0 untuk Perempuann. \nGender: "))

        if usia >=2 and usia <=18:
            if gender == 1:
                print("Rekomendasi Asupan Air = 1.6 Liter")
            elif gender == 0:
                print("Rekomendasi Asupan Air = 1.4 Liter")
        elif usia >=18 and usia <=64:
            if gender == 1:
                print("Rekomendasi Asupan Air = 2.5 Liter")
            elif gender == 0:
                print("Rekomendasi Asupan Air = 2.0 Liter")
        elif usia >=65:
            if gender == 1:
                print("Rekomendasi Asupan Air = 2.0 Liter")
            elif gender == 0:
                print("Rekomendasi Asupan Air = 1.8 Liter")
        elif usia <2:
            if gender ==1:
                print("Masih Diberi ASI")
            elif gender ==0:
                print("Masih Diberi ASI")
    except ValueError:
        print("Coba lagi")