#Örnek: 1634 = 14 + 64 + 34 + 44 = 1634
#Kullanıcıdan alınan bir sayının "Armstrong" sayısı olup olmadığını bulan yazılımı python dilinde programlayınız.

sayi=input("Kontrol edilmek istenen basamaklı sayıyı giriniz :")
liste=list(sayi)
toplist=[]
for i in liste:
    i=int(i)**4
    toplist.append(i)
p=sum(toplist)
if p==int(sayi):
    print("sayı armstrong sayısıdır...")
else:
    print("sayı armstrong sayısı değildir...")