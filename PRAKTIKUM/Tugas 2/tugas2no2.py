translate = {   #mendeklarasikan variabel sebagai dictionary yang sudah diisi
    "you":"kamu",   #value dari "you" adalah "kamu"
    "sorry":"maaf", #value dari "sorry" adalah "maaf"
    "egg":"telur",  #value dari "egg" adalah "telur"
    "bottle":"botol",   #value dari "bottle" adalah "botol"
    "chair":"kursi"     #value dari "chair" adalah "kursi"
}
put=input("Masukkan Kata: ")    #menginputkan kata yang ingin di terjemahkan
print("===Penerjemah B.Inggris===") 
if put in translate:    #jika input nya ada di dalam dictionary
    print(f"{put} -> ",translate[put])  #maka akan menampilkan terjemahannya yang berada di dalam dictionary sesuai kata yang diinputkannya
else:   #jika inputannya tidak ada didalam dictionary
    print("Kata tidak ditemukan!")  #maka akan menampilkan output bahwa kata yang diinputkannya tidak ada di dalam dictionary
input()