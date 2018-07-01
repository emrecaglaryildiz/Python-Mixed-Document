giris=input("şifrelenmek istenen 8 harfli/rakamlı , kelimeyi/sayıyı giriniz :")
a=[]
a=giris
b=[]
for harf in a:
    b.append(harf)
print(str(ord(b[0]))+
      str(ord(b[1]))+
      str(ord(b[2]))+
      str(ord(b[3]))+
      str(ord(b[4]))+
      str(ord(b[5]))+
      str(ord(b[6]))+
      str(ord(b[7])))