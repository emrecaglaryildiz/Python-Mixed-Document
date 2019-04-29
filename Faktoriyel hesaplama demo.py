# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 13:59:19 2019

@author: Emre YILDIZ
"""

#Faktoriyel hesaplama demo

sayi= int(input("Faktoiyeli sorgulanan sayı giriniz : "))
fakt=1

if sayi<0:
    print("sayı negatiftir.")
elif sayi==0:
    print("1")
else:
    for i in range(1,(sayi+1)):
        fakt=fakt*i
        
print("Sonuç ",fakt)