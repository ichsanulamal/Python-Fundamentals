# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 15:53:07 2019

@author: muhammad.ichsanul91
"""

#Masukkan dari user
z = input('Masukkan nama file:')
r1 = int(input('Masukkan r1:'))
r2 = int(input('Masukkan r2:'))
c1 = int(input('Masukkan c1:'))
c2 = int(input('Masukkan c2:'))

#Buka file untuk dibaca
f = open(z, 'r')
#Memisahkan baris
split = f.read().split('\n')


#untuk setiap baris    
for index in range(len(split)):
    kosong = []
#Jika index tambah 1 nya r1 maka     
    if (index +1) == r1:
        kosong = (split[index:r2])
        for angka in kosong:
           kosong = angka.split()
           baris = kosong[(c1-1):(c2)]
           for i in baris:
               print(i, end=' ')
           print() 
           
f.close()
        
        
        
    
    
        
        
    

        
    


