# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 13:43:37 2019

@author: M. Ichsanul Amal
"""

#Import library numpy untuk mengatur dan matplotlib untuk membuat grafik
import matplotlib.pyplot as plt
import numpy as np

#Definisi untuk mencetak bagian awal program
def header():
    awalan = 'Masukkan pesan: (untuk berhenti masukkan string kosong)'
    print('='*(len(awalan)))
    print(awalan)
    print('='*(len(awalan)))

#Definisi yang mengembalikan list konjungsi atau stopword 
def lststopword():
    #Membuka dan menyalin seluruh isi dari file
    file = open('TP2-stopword.txt', 'r')
    write = file.readlines()
    #Membuat list kosong yang akan dimasukkan kata stopword
    konjungsi =[]
    for i in write:
        i = i.replace('\n', '')
        konjungsi.append(i)
    file.close()
    
    return konjungsi
    
#Definisi yang mengembalikan list kata tanpa kata berulang
def lstkata(x):
    katasaja = []
    for kata in x:
        if kata not in katasaja:
            katasaja.append(kata)
    return katasaja

#Definisi membuat tabel    
def tabel(x):
    #Untuk Formatting tabel
    format_tabel = '{:>4}{:^1}{:<20}{:^15}'
    print('Distribusi frekuensi kata:')
    print('-'*40)
    print(format_tabel.format('No', ' ', 'Kata', 'Frekuensi'))
    print('-'*40)
    for i in range(len(lstkata(x))):
        print(format_tabel.format(i+1, ' ', lstkata(x)[i], x.count(lstkata(x)[i])))
    print('-'*40)

#Definisi membuat grafik        
def grafik(x):
    jumlah = []
    for i in range(len(lstkata(x))):
        jumlah.append(x.count(lstkata(x)[i]))
    
    index = np.arange(len(lstkata(x)))
    plt.barh(index, jumlah[::-1])
    plt.yticks(index, lstkata(x)[::-1], fontsize ='8')
    plt.xlabel('Frekuensi')
    plt.title('Frekuensi Kemunculan Kata')
   
    plt.show()
        
#Panggil fungsi untuk mencetak bagian awal
header()

#Meminta user untuk menginput kata atau kalimat atau paragraf
x = 'kosong'
kalimat_baru = ''
#Berhenti saat input yang dimasukkan adalah string kosong
while x != '':
    x = input('Pesan:')
    kalimat_baru += x + ' '
else:
    print('*'*50)
   
#Memisahkan kata pada kalimat atau paragraf
list_kata = kalimat_baru.split()

#String kosong untuk dimasukkan huruf atau angka atau strip
kalimat_baruv2 = ''
#Scan tiap huruf untuk mendapatkan hanya alphabet, angka, dan tanda strip
for kata in list_kata:
    kalimat_baruv2 += ' '
    for huruf in kata:
        if huruf.isalpha():
            kalimat_baruv2 += huruf.lower()
        elif huruf.isalnum():
            kalimat_baruv2 += huruf
        elif huruf == '-':
            kalimat_baruv2 += huruf

kalimat_baruv2 = kalimat_baruv2.split()
kalimat_baruv3 = ''

#Membuang kata yang ada di dalam stopword dan strip yang ada di kiri kanan             
for kata in kalimat_baruv2:
    if kata in lststopword():
        kalimat_baruv3 += ''    
    elif kata[0] == '-':
        kalimat_baruv3 += kata.replace('-','') + ' '
    elif kata[-1] == '-':
        kalimat_baruv3 += kata.replace('-','') + ' '
    elif kata.count('-') > 1 or len(kata) <2:
        kalimat_baruv3 += ''   
    else:
        kalimat_baruv3 += kata + ' '
#Membuat list kalimat baru
kalimat_baruv3 = kalimat_baruv3.split()

#Panggil fungsi untuk membuat tabel dan grafik
tabel(kalimat_baruv3)
grafik(kalimat_baruv3)


'''        
Halo, Bunga. Apa kabar kamu? Apakah baik-baik saja?? 
Baik! 
Apakah kamu sudah mengerjakan TP2 (DDP-1) !? 
Belum! Dan kamu? 
Aku juga belum, hehe... Masih 'sibuk' ! 
Ayo belajar bersama, katanya kita harus mempelajari library Matplotlib 
untuk menggambar grafik. 
Oh, ya? Menarik sekali! 
Kamu sudah membaca soal tampaknya ;-)              
'''
