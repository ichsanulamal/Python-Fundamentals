# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 16:26:43 2019

@author: muhammad.ichsanul91
"""

permen_biru = int(input("Masukkan banyak permen biru yang dimiliki:"))
promo_toko = int(input("Masukkan nilai X:"))

if permen_biru > 0 and promo_toko > 0:
    banyak_permen_merah = int(permen_biru / promo_toko)
    sisa_biru = (permen_biru % promo_toko)
    print("Pak Chanek memiliki", banyak_permen_merah, "permen merah")
    print("dengan", sisa_biru, "permen biru yang tersisa")
    
else:
    print("Tidak ada banyak permen negatif atau Tidak ada promo toko negatif atau Anda tidak memasukkan angka!")
    