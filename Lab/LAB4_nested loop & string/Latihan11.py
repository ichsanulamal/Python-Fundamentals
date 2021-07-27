teks = input('Masukkan teks:')
output = ''
cekkata = teks.split()

count = 0

for i in cekkata:
    
    if i == 'wk' * (len(i) // 2):
        count += 1
        i = i.upper()
    print(i, end= ' ')

print('', sep='')
print('', sep='')
print('Tertawa wkwk sebanyak', count, 'kali')



#Hadeeeuuuhhh
                
            
            
          
            
            

        
    
        
        
