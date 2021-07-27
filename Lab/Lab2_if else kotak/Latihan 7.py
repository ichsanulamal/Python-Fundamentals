# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
sisi_persegi = int(input('Masukkan panjang sisi persegi:'))
x = int(input('Masukkan komponen X dari titik kiri bawah persegi:'))
y = int(input('Masukkan komponen Y dari titik kiri bawah persegi:'))
p = int(input('Masukkan komponen X dari titik yang ingin dicek:'))
q = int(input('Masukkan komponen Y dari titik yang ingin dicek:'))

"""
Meminta user menginput sisi persegi,
komponen X dari titik kiri bawah persegi,
komponen Y dari titik kiri bawah persegi,
komponen X dari titik yang ingin dicek,
komponen Y dari titik yang ingin dicek.
"""

if p >= x and q >= y:
    if p == x or q == y:
        print('Di tepi')
    elif p < (x + sisi_persegi) and q < (y + sisi_persegi):
        print('Di dalam')
else: 
    print('Di luar')
    
# Logika saya hanya jalan untuk 3 kasus. Spatial saya kurang terlatih
# Mohon dimaafkan :))
    


