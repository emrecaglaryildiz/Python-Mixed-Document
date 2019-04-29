# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:39:09 2019

@author: Emre YILDIZ
"""

# selamlama fonksiyonu
def selamVer(isim="ziyaretçi"):
    print("merhaba "+isim)    
selamVer()


# üçgena alan hesaplama fonksiyonu
def dikucgenalani(a,b):
    return print((a*b)/2)
dikucgenalani(3,4)


#lambda fonksiyon tanımlama
dikucgenalanhesap=lambda a,b:a*b/2
print(dikucgenalanhesap(3,4))


#fonksiyon ataması
dikucgenalanhesap=lambda a,b:a*b/2
x=dikucgenalanhesap
print(x(3,4))