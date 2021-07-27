# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:07:57 2019

@author: muhammad.ichsanul91
"""

LP_player = 1000 
LP_enemy = 1000
#LP player dan musuh di awal

while LP_player > 0 and LP_enemy > 0:
#Selalu menjalankan perintah saat LP player atau LP musuh tidak 0
    print('------------------------')
    print('LP Anda:', LP_player)
    print('LP Musuh:', LP_enemy)
    print('------------------------')
    print('Apa yang ingin Anda lakukan?')
    print('1. Serang dengan scratch (100 LP)')
    print('2. Serang dengan throw (300 LP)')
    print('3. Serang dengan flamethrower (500 LP)')
    print('4. Tangkap musuh Anda')
    
    pilihan_game = int(input('Masukkan nomor pilihan:'))
    #Meminta player memasukkan perintah

    if pilihan_game == 1:
        LP_enemy -= 100
#pilihan 1 mengurangi LP musuh 100 poin
        
        print('Anda menggunakan scratch dan mengurangi LP musuh sebanyak 100 poin. ')


    elif pilihan_game == 2:
        LP_enemy -= 300
#pilihan 2 mengurangi LP musuh 300 poin

        print('Anda menggunakan throw dan mengurangi LP musuh sebanyak 300 poin.')

        
    elif pilihan_game == 3:
        LP_enemy -= 500

#pilihan 3 mengurangi LP musuh 500 poin

        print('Anda menggunakan flamethrower dan mengurangi LP musuh sebanyak 500 poin.') 

        
#pilihan 4 tangkap musuh
    elif pilihan_game == 4 and LP_enemy <= 500 :
#Berhasil apabila LP musuh <= 500
        print('Anda berhasil menangkap musuh Anda!')
        break

#Gagal apabila LP musuh > 500
    else:
        if pilihan_game == 4 and LP_enemy > 500 :
            LP_player -= 200
            print('Anda mencoba menangkap musuh Anda, namun gagal!')
            print('Musuh Anda menggunakan slap dan mengurangi LP Anda sebanyak 200 poin.')
        

    if LP_enemy <= 0:
        print('Anda menang!')
        break
    print('LP musuh yang tersisa sebanyak', LP_enemy, 'poin.')
    
    if LP_player <= 0:
        print('Anda kalah!')
        break
    
    LP_player -= 200
    print('Musuh Anda menggunakan slap dan mengurangi LP Anda sebanyak 200 poin.')
    print('LP Anda yang tersisa sebanyak', LP_player, 'poin.')

    

        
        
 
        
    

    
    



