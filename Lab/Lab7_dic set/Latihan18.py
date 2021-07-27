# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 15:57:40 2019

@author: muhammad.ichsanul91
"""

   
print('Masukkan data:')

dict_siswa = {}
dict_penyusup = {}
x = 'haha'

while x != ['']:
    x = input().split(',')
    if x[-1] == 'True':
        dict_siswa[x[0]] = x[1::]
    elif x[-1] == 'False':
        dict_penyusup[x[0]] = x[1::]

print('Peserta:\nJumlah:', len(dict_siswa))

dict_siswa_baru = {}
for key, values in dict_siswa.items():
    if values[0] not in dict_siswa_baru: 
        dict_siswa_baru[values[0]] = [key] 
    else: 
        val_sementara = [key] + dict_siswa_baru[values[0]] 
        dict_siswa_baru[values[0]] = val_sementara


     
for key, item in dict_siswa_baru.items():
    print(key, ':', len(item))
    for i in item:
        print('- ' + i)
    print()
           
    
print('---------------------------------------------------')

print('Penyusup:\nJumlah:', len(dict_penyusup))
dict_penyusup_baru = {}
for key, values in dict_penyusup.items():
    if values[0] not in dict_penyusup_baru: 
        dict_penyusup_baru[values[0]] = [key] 
    else: 
        val_sementara = [key] + dict_penyusup_baru[values[0]] 
        dict_penyusup_baru[values[0]] = val_sementara

     
for key, item in dict_penyusup_baru.items():
    print(key, ':', len(item))
    for i in item:
        print('- ' + i)
    print()
    
    

    
