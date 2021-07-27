# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:31:40 2019

@author: muhammad.ichsanul91
"""

#Fungsi yang mengembalikan list angka di matrix
def baca_mtr(x):
    string = ''
    print('Masukkan matriks', x, ':') 
    p = str(input('Masukkan dimensi (baris dan kolom, dipisah oleh spasi):')).split() 
    for i in range(int(p[0])):
        q = str(input())
        string += q + ' '
    return string.split()
    
#Fungsi yang mendeteksi apakah isi kedua matrix sama atau tidak          
def list_sama(list1, list2):
    
    lst1_dict = {}
    lst2_dict = {}
    
    for word in list1:
        if word in lst1_dict:
            lst1_dict[word] += 1
        else:
            lst1_dict[word] = 1
            
    for word in list2:
        if word in lst2_dict:
            lst2_dict[word] += 1
        else:
            lst2_dict[word] = 1
    
    if lst1_dict == lst2_dict:
        return True
    return False

lst1 = baca_mtr('pertama')
lst2 = baca_mtr('kedua')

if list_sama(lst1, lst2):
    print('Isi matriks sama!')
else:
    print('Isi matriks berbeda!')
    
    
    
    
