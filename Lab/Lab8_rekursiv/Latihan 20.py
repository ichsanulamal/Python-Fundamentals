# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:52:17 2019

@author: muhammad.ichsanul91
"""

def maks_tuple(t):
    jumlah = 0
    jumlah = maks_nilai(t, jumlah)
    
    if jumlah == 0:
        return None
    return jumlah

def maks_nilai(t, highest):
    try:
        for item in t:
            if type(item) != int:
                highest = maks_nilai(item, highest)
            else:
                if item > highest:
                    highest = item
        return highest
    except:
        highest = t
        return highest
    

if __name__ == '__main__':
    tup1 = (1,2,3,4)
    print(tup1, '->', maks_tuple(tup1))
    tup2 = (1,(2,5),(1,(((9)))))
    print(tup2, '->', maks_tuple(tup2))
    tup3 = ((), (((((()))))), ((), (()), ()))
    print(tup3, '->', maks_tuple(tup3))
    tup4 = ()
    print(tup4, '->', maks_tuple(tup4))
