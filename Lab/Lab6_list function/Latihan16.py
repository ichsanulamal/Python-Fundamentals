# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 16:05:46 2019

@author: muhammad.ichsanul91
"""

#Fungsi yang mengembalikan nilai string
def baca_list():
    return str(input(''))
    
#Fungsi yang mendeteksi apakah isi kedua list sama atau tidak     
def list_sama(list1, list2):
    #Mengubah keduanya menjadi list
    list1.split()
    list2.split()
    
    lst1_dict = {}
    lst2_dict = {}
    
    #Menghitung jumlah angka di kedua list
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
    
    #Jika dictionary(list1) = dictionary(list2) sama,
    #kembalikan nilai True
    if lst1_dict == lst2_dict:
        return True
    return False
            
        
    
print('Masukkan list pertama (angka dipisah oleh spasi):')
list_1 = baca_list()
print('Masukkan list kedua (angka dipisah oleh spasi):')
list_2 = baca_list()


if list_sama(list_1, list_2):
    print('Isi list sama!')
else:
    print('Isi list berbeda!')

    

    