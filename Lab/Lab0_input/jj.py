

nama_coin_1 = input("Nama coin 1:")
harga_beli_1 = int(input("Harga beli coin 1:"))
harga_saat_ini_1 = int(input("Harga coin 1 saat ini:"))
keuntungan_1 = (harga_saat_ini_1 - harga_beli_1) * 100 / harga_beli_1  
#'profit1 = TO DO : tuliskan keuntungan/kerugian dari coin 1'

nama_coin_2 = input("Nama coin 2:")
harga_beli_2 = int(input("Harga beli coin 2:"))
harga_saat_ini_2 = int(input("Harga coin 2 saat ini:"))
keuntungan_2 = (harga_saat_ini_2 - harga_beli_2) * 100 / harga_beli_2  
#profit2 = '#TO DO : tuliskan keuntungan/kerugian dari coin 2'

format_barisan = "{:>5}|{:^20}|{:^15}|{:^15}|{:^10}"

print("\nRiwayat Pembelian Mata Uang Kripto")
print(format_barisan.format("No.", "Nama Coin", "Harga Beli", "Harga Sekarang", "Keuntungan"))
print(format_barisan.format("-" * 5, "-" * 20, "-" * 15, "-" * 15, "-" * 5))

print(format_barisan.format("1", nama_coin_1, harga_beli_1, harga_saat_ini_1, str(keuntungan_1)+"%"))
print(format_barisan.format("2", nama_coin_2, harga_beli_2, harga_saat_ini_2, str(keuntungan_2)+"%"))
