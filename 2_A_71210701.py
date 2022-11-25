print("===== Selamat datang di Toko Andi Tersenyum, selamat berbelanja! =====")
total = int(input("Total belanja :Rp."))

if total < 100_000:
    print("Tidak ada diskon! Maka yang anda bayarkan adalah: Rp. ",total)
elif total >= 1_000_000:
    print("Biaya yang harus dibayar setelah diskon adalah: Rp. ", total-(total*0.10))
elif total >= 500_000:
    print("Biaya yang harus dibayar setelah diskon adalah: Rp. ", total-(total*0.05))
else:
    print("Biaya yang harus dibayar setelah diskon adalah: Rp. ", total-(total*0.02))


