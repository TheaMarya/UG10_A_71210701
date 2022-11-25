NAME_mhs = input("Masukkan nama mahasiswa : ")
NIM_mhs = (input("Masukkan NIM-nya : "))


if NIM_mhs[0:2] == '71' and int(NIM_mhs[2:4]) <= 22 and int(NIM_mhs[2:4]) >= 20:
    
    print(NAME_mhs, "Merupakan mahasiswa informatika angkatan 20 hingga 22")

else:
    print("bukan mahasiswa informatika angktan 20 hingga 22")