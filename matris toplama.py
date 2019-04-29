# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 14:05:06 2019

@author: Emre YILDIZ
"""

#matris toplama

x=[[1,2,3],[3,4,5],[6,5,3]]
y=[[1,4,3],[6,4,2],[9,5,7]]
sonuc=[[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j]=x[i][j]+y[i][j]

print(sonuc)
