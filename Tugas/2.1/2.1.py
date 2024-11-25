def main():
    while True:
        a = input("Apakah anda berolahraga? (y/n):  ")
        if a == "y":
            a = "--> Membantu kualitas tidur.\n"
            print(a)
            break
        else:
            print("--> Tidak membantu kualitas tidur dan tetap insomnia.\n")
            main()
    while True:
        a = input("Apakah anda tidur di siang hari? (y/n):  ")
        if a == "n":
            a = "--> Malamnya mengantuk.\n"
            print(a)
            break
        else:
            print("--> Malamnya tidak mengantuk dan anda tetap insomnia.\n")
            main()
    while True:
        a = input("Apakah anda bermain hp sebelum tidur? (y/n):  ")
        if a == "n":
            a = "--> Bisa tidur.\n"
            print(a)
            break
        else:
            print("--> Malamnya tidak tidak bisa tidur dan anda tetap insomnia.\n")
            main()


a = ("Anda Insomnia")
print(f"--> Kondisi anda = {a}")
main()
a = ("Tidak insomnia")
print(f"--> Kondisi anda = {a}")
input()