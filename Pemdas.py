# Program untuk membantu mengatasi insomnia

def main():
    print("Anda Mengalami Insomnia")
    
    while True:
        olahraga = input("Apakah Anda berolahraga? (y/n): ").lower()
        if olahraga == "y":
            print("Membantu kualitas tidur.")
            
            # Melanjutkan ke pertanyaan tidur siang
            while True:
                tidur_siang = input("Apakah Anda tidur di siang hari? (y/n): ").lower()
                if tidur_siang == "y":
                    print("Malamnya tidak mengantuk.")
                    print("Anda tetap insomnia.")
                    break  # Kembali ke pertanyaan awal tentang olahraga
                
                elif tidur_siang == "n":
                    print("Malamnya mengantuk.")
                    
                    # Lanjutkan ke pertanyaan tentang penggunaan HP
                    while True:
                        main_hp = input("Apakah Anda main HP sebelum tidur? (y/n): ").lower()
                        if main_hp == "y":
                            print("Tidak bisa tidur.")
                            break  # Kembali ke pertanyaan awal tentang olahraga
                        elif main_hp == "n":
                            print("Anda bisa tidur.")
                            print("Selamat, masalah insomnia teratasi.")
                            return  # Mengakhiri program
                        else:
                            print("Jawaban tidak valid, masukkan 'y' atau 'n'.")
                else:
                    print("Jawaban tidak valid, masukkan 'y' atau 'n'.")
        
        elif olahraga == "n":
            print("Tidak membantu kualitas tidur.")
            print("Anda tetap insomnia.")
        else:
            print("Jawaban tidak valid, masukkan 'y' atau 'n'.")

# Menjalankan program
main()
