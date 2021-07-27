# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 14:10:47 2019

@author: ICHSAN
"""

import csv

#Membaca file info yang berisikan tentang info program
def info(): #File info.txt dalam zip
    file = open('info.txt', 'r')
    write = file.read()
    file.close()
    return write
    
#Memisahkan dan mengembalikan perintah dan isinya 
def cari_order(x):
    x = x.split()
    nilai = ' '.join(x[1::])
    return x[0], nilai #x[0] dan nilai adalah perintah dan isinya
    
#Mengimpor file dan menjadikannya sebagai dictionary
#key adalah nama budaya
#value adalah list yang berisi tipe, provinsi, dan link
def impor(a):
    f = open(a, newline='')
    reader = csv.reader(f)
    
    ldictb = []
    for baris in reader:
        ldictb.append(baris)
        if [] in ldictb:
            ldictb.remove([])
        
    dictb = {}
    for lst in ldictb:
        dictb[lst[0]] = lst[1:]
    f.close()
    return dictb

#Mengekspor isi yang bertipe dictionary ke dalam file
def ekspor(isi, file):
    f = open(file, 'w')
    w = csv.writer(f)
    
    count = 0
    for key,value in isi.items():
        w.writerow([key] + value) # [key] + value = list
        count += 1
    f.close()
    return count
    
#Tabel manual formatting
def tabel(tupoflist): 
    formtab = '{:20}|{:15}|{:20}|{:40}'
    print("-" * 98)
    print(formtab.format('Nama Kebudayaan', 'Tipe', 'Asal Daerah', 'Link'))
    print(formtab.format("-" * 20, "-" * 15, "-" * 20, "-" * 40))
    for lst in tupoflist:
        print(formtab.format(lst[0], lst[1], lst[2], lst[3]))
    print()

#Mencari nama budaya dalam file
def cari_nama(x, file):
    if x == '*':
        lst = []
        for key, value in impor(file).items():
            lst.append(tuple([key] + value))
        if len(lst) >0:
            tabel(lst)
        else:
            print('*Tidak ditemukan data kebudayaan*')
           
    else:
        try:
            print(x + ',' + ','.join(impor(file)[x]))
        except KeyError:
            print(x, 'tidak ditemukan')
        
        
#Mencetak setiap budaya yang ada dalam tipe di file  
def cari_tipe(x, file):    
    lst = []
    count = 0
    for key, value in impor(file).items():
        if x in value: #Mencari apakah x ada di list value
            lst.append([key] + value)
            count += 1

    if len(lst) >0:
        tabel(lst)
    else:
        print()
    print('*Ditemukan', count, 'tipe', x +'*')
        
#Mencetak setiap budaya yang ada dalam provinsi di file    
def cari_prov(x, file): 
    lst = []
    count = 0
    for key, value in impor(file).items():
        if x in value:
            lst.append([key] + value)
            count += 1

    if len(lst) >0:
        tabel(lst)
    else:
        print()
    print('*Ditemukan', count, 'Warisan Budaya*')

#Menambahkan budaya ke dalam file    
def tambah(x, y= 'file.csv'):
    x = x.split(';;;')
    if len(x) == 4:
        if x[0] not in impor(y):
            f = open(y, 'a')
            w = csv.writer(f)
            w.writerow('')
            w.writerow(x)
            print(x[0], 'ditambahkan')
        else:
            print('kebudayaan', x[0], 'sudah ada, gunakan UPDATE untuk mengupdate data kebudayaan')
    elif len(x)<4:
        print('Input yang anda masukkan kurang lengkap')
    else:
        print('Input yang anda masukkan terlalu banyak')

#Update budaya dengan value yang baru       
def update(x, file):
    p = impor(file)
    x = x.split(';;;')
    if len(x) == 4:
        if x[0] in p:
            p[x[0]] = x[1::]
            ekspor(p, file)
            print(x[0], 'diupdate')
                
        else: #Error apabila tidak ada
            print('tidak ada kebudayaan bernama', x[0], 'di data kebudayaan')           
    elif len(x)<4:
        print('Input yang anda masukkan kurang lengkap')
    else:
        print('Input yang anda masukkan terlalu banyak')   

#Menghapus item pada file lalu mengekspor ke file sebelumnya
def hapus(x, file):
    p = impor(file)
    try:
        del p[x]
        ekspor(p, file)
        print(x, 'dihapus')    
    except KeyError:
        print('Tidak ada budaya bernama', x)
    
#Mencetak jumlah kebudayaan   
def stat(x):
    print('Terdapat', len(impor(x)), 'warisan budaya') 

#Mencetak jumlah budaya dalam tiap tipe yang ada dalam file    
def stat_tipe(x):
    p = impor(x)
    dictnew = {}
    for value in p.values(): 
        if value[0] in dictnew:
            dictnew[value[0]] += 1
        else:
            dictnew[value[0]] = 1
    lst = []
    for key,value in dictnew.items():
        lst.append([value, key])
    lst = sorted(lst)[::-1]
    print('Dalam data,')
    for item in lst:
        print('kebudayaan dengan tipe', item[1], 'sebanyak:', item[0])
        
#Mencetak jumlah budaya dalam tiap provinsi yang ada dalam file  
def stat_prov(x):
    p = impor(x)
    dictnew = {}
    for value in p.values(): 
        if value[1] in dictnew:
            dictnew[value[1]] += 1
        else:
            dictnew[value[1]] = 1
    lst = []
    for key,value in dictnew.items():
        lst.append([value, key])
    lst = sorted(lst)[::-1]
    print('Dalam data,')
    for item in lst:
        print('kebudayaan yang berasal dari', item[1], 'sebanyak:', item[0])
                           
#Pemanggilan fungsi info  
info = info()

#Mencetak bagian pembuka program
print('##### \nBudayaKB Lite v1.0 \n~Kalau bukan kita yang melestarikan budaya, siapa lagi?~ ')
print('Ketik "INFO" untuk mengetahui fitur program')

#Memulai program
kata = '' 
while kata != 'KELUAR':
    print('#####')
    kata = input('> Masukkan perintah:')
    try:
        order, nilai = cari_order(kata)
    except: #Jika input hanya enter (IndexError)
        print('Perintah tidak dikenal')
        continue
    if order == 'INFO':
        print()
        print(info)           
    elif order == 'IMPOR':
        try :
            print('Terimpor', len(impor(nilai)), 'baris')
            file_prev = nilai
        except:
            print('File yang anda masukkan tidak ada')
    elif order == 'CARINAMA':
        try:
            cari_nama(nilai, file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'CARITIPE':
        try:
            cari_tipe(nilai, file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'CARIPROV':
        try:
            cari_prov(nilai, file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'TAMBAH':
        try:
            tambah(nilai, file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'UPDATE':
        try:
            update(nilai, file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'HAPUS':
        try:
            hapus(nilai, file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'STAT':
        try:
            stat(file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'STATTIPE':
        try:
            stat_tipe(file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'STATPROV':
        try:
            stat_prov(file_prev)
        except:
            print('Anda belum mengimpor file')
    elif order == 'EKSPOR':
        try:
            print('Terekspor', ekspor(impor(file_prev), nilai), 'baris')    
        except:
            print('Anda belum mengimpor file')
    elif order == 'KELUAR':
        print('~Sampai jumpa, jangan lupa mencintai warisan budaya Indonesia!~')    
    else:
        print('Perintah tidak dikenal')

                


'''
tes:
tipe = ('IMPOR', 'EKSPOR', 'CARINAMA', 'CARITIPTE', 'CARIPROV', 'TAMBAH', 'UPDATE', 'HAPUS', 'STAT', 'STATTIPE', 'STATPROV', 'KELUAR')    
Rendang,Makanan,Sumatra Barat,http://dbpedia.org/resource/Rendang 
Tari Saman,Tarian,Aceh,http://dbpedia.org/resource/Saman_(dance) 
Nasi Gandul,Makanan,Jawa Tengah,https://www.wikidata.org/wiki/Q12500151 
Tari Gambyong,Tarian,Jawa Tengah,https://id.wikipedia.org/wiki/Tari_Gambyong
'''

    
