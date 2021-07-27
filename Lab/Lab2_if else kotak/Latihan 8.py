# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 16:21:40 2019

@author: muhammad.ichsanul91
"""

sisi_persegi = int(input('Masukkan panjang sisi persegi:'))
x = int(input('Masukkan komponen X dari titik kiri bawah persegi pertama:'))
y = int(input('Masukkan komponen Y dari titik kiri bawah persegi pertama:'))
p = int(input('Masukkan komponen X dari titik kiri bawah persegi kedua:'))
q = int(input('Masukkan komponen Y dari titik kiri bawah persegi kedua:'))

"""
Meminta user menginput sisi persegi,
komponen X dari titik kiri bawah persegi pertama,
komponen Y dari titik kiri bawah persegi pertama,
komponen Y dari titik kiri bawah persegi kedua,
komponen Y dari titik kiri bawah persegi kedua.


if y + sisi_persegi == q and x + sisi_persegi == p:
    print('persegi terpisah')
elif p + sisi_persegi > x and y + sisi_persegi > q:
    print('Persegi beririsan')
elif y == q and p + sisi_persegi == x:
    print('persegi beririsan')
elif y == q and p + sisi_persegi < x:
    print('Persegi terpisah')
    
"""    
# Logika saya hanya jalan untuk 4 kasus. Spatial saya kurang terlatih
# Mohon dimaafkan :))



if (x + sisi_persegi <= p and y + sisi_persegi <= q) or (p + sisi_persegi <= x and q + sisi_persegi <= y):
    print("persegi beririsan")

