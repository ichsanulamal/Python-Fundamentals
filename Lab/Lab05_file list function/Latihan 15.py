# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:18:29 2019

@author: muhammad.ichsanul91
"""

def isi_list(pengen_isi, baris, kolom):
    #harusnya -28 agar mulai dari 0
    namron_punya_cnt = 0
    #jadi kode barunya adalah
    namron_punya_cnt = -28
    for i in range(baris):
        if i % 2 == 0:
            for j in range(kolom):
                pengen_isi[i][j] = namron_punya_cnt
                namron_punya_cnt += 1
        else:
            for j in range(kolom - 1, -1, -1):
                pengen_isi[i][j] = namron_punya_cnt
                namron_punya_cnt += 1

def cetak_list(pengen_cetak, baris, kolom):
    for i in range(5):
        for j in range(7):
            print(namron_punya_list[i][j], end=' ')
        print()

            
namron_punya_list = [[0] * 7] * 5
isi_list(namron_punya_list, 5, 7)
cetak_list(namron_punya_list, 5, 7)