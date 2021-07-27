# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:03:26 2019

@author: muhammad.ichsanul91
"""

def cibonacci(n):
    global tanggal
    global bulan
    
    if n == 0:
        return 0
    elif n == 1:
        return tanggal
    elif n == 2:
        return bulan
    else:
        return cibonacci(n-1) + cibonacci(n-2)
    
x = input('Masukkan tanggal undian:').split(',')

angka_awal = x[2][-2:]
angka_akhir1 = x[2][:2] 

tanggal = int(x[0])
bulan = int(x[1])
lompatan = int(x[2][2:])

angka_tengah = cibonacci(lompatan) 

print('Angka pemenang:', angka_awal, angka_tengah, angka_akhir1)
    
    
    
# 2 3 5 8 13 21