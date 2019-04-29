# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 14:29:27 2019

@author: Emre YILDIZ
"""

sozluk={
        "book":"kitap",
        "pencil":"kalem"
        }

sozluk2={
        "defter":"notebook",
        "silgi":"eraser"
        }


sozluk["book"] = "kitap 1"  #güncelleme
del(sozluk2["silgi"])       #silme

print(sozluk)
print(sozluk2)
print(sozluk2["defter"])
print(sozluk["book"])

