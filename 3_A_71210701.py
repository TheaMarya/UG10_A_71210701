a = int(input("Masukkan nilai soal 1: "))
b = int(input("Masukkan nilai soal 2: "))
c = int(input("Masukkan nilai soal 3: "))
umur = int(input("Masukkan umur anda: "))
hasil = (a*0.5) + (b*0.3) + (c*0.2)
print("Rata-rata nilai Anda: ",hasil)

if umur <= 25:
    if hasil >= 80:
        print("selamat anda lulus!")
    else:
        print("Coba lagi tahun depan!")
else:
    if hasil >= 90:
        print("selamat anda lulus!")
    else:
        print("Coba lagi tahun depan!")