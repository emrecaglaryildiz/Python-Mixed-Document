# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:19:45 2019

@author: Emre YILDIZ
"""

#kelime sıralama

cumle=input("cümle giriniz : ")

kelimeler=cumle.split()
kelimeler.sort()

#direk yazma

print(kelimeler)

#for ile yazma

for i in kelimeler:
    print (i)


