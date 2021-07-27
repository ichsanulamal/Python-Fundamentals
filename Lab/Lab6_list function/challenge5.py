# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:14:33 2019

@author: muhammad.ichsanul91
"""

N = int(input('Masukkan nilai N:'))
M = input('Masukkan isi list (angka 1 sampai N, dipisah oleh spasi):\n').split()

for i in M:
    if M.count(i) > 1:
        print('Bilangan duplikat:', i)
        break
    
 