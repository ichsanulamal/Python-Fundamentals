n = int(input('N'))

spasi = n - 4

if n % 2 == 0 and n >= 4:
    for i in range((n-2)//2):
        print('|', ' '* i, '\\', ' '*spasi, '/', ' '*i, '|', sep= '')
        spasi -= 2

    spasi = 0
    for j in range(((n-2)//2 - 1), -1, -1):
        print('|', ' '* j, '/', ' '*spasi, '\\', ' '*j, '|', sep= '')
        spasi += 2

    print(1,2,3,4)

else:
    print('input yang anda masukkan salah')
                   

                   
        
