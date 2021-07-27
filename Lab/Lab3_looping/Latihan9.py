# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 15:56:49 2019

@author: muhammad.ichsanul91
"""

n = int(input('Masukkan daftar angka yang akan diprint(1 sampai 1000):'))
#Masukkan daftar angka

if n < 1 or n > 1000:
    print('Maaf, input yang anda masukkan salah')
#Tidak mencetak apabila input yang dimasukkan kurang dari 1 atau lebih dari 1000
else:
    for i in range(1,n+1):
        if i % 21 == 0:
            print('BingBung!') # Prioritas habis dibagi 21
        elif i % 7 == 0:
            print('Bung!')
        elif i % 3 == 0:
            print('Bing!')
        else:
            print(i) # Cetak i apabila tidak habis dibagi 3, 7, atau 21
