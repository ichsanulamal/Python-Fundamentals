# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:41:18 2019

@author: muhammad.ichsanul91
"""

nama_permen_1 = input("Nama permen 1:")
harga_beli_1 = int(input("Harga beli permen 1:"))
profit_permen_1 = int(input("Profit permen 1:"))

nama_permen_2 = input("Nama permen 2:")
harga_beli_2 = int(input("Harga beli permen 2:"))
profit_permen_2 = int(input("Profit permen 2:"))

nama_permen_3 = input("Nama permen 3:")
harga_beli_3 = int(input("Harga beli permen 3:"))
profit_permen_3 = int(input("Profit permen 3:"))

format_barisan = "{:>5}|{:^20}|{:^15}|{:^15}"

print(format_barisan.format("No.", "Nama Permen", "Harga Beli", "Harga Jual"))
print(format_barisan.format("-" * 5, "-" * 20, "-" * 15, "-" * 15))

print(format_barisan.format("1", nama_permen_1, harga_beli_1, profit_permen_1 / 100 * harga_beli_1 + harga_beli_1))
print(format_barisan.format("2", nama_permen_2, harga_beli_2, profit_permen_2 / 100 * harga_beli_2 + harga_beli_2))
print(format_barisan.format("3", nama_permen_3, harga_beli_3, profit_permen_3 / 100 * harga_beli_3 + harga_beli_3))