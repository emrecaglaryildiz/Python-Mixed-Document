#2 üzeri 15 = 32768 ve basamaklarının toplamı 3 + 2 + 7 + 6 + 8 = 26 'dır.
#klavyeden girilecek x ve y sayılarından oluşacak xy sayısının değerinin basamakları toplamını hesaplayan yazılımı python dilinde yazınız.

x=input("sayı giriniz : ")
y=input("üst olacak sayıyı : ")

üstlüsayi=int(x)**int(y)

basamak=list(str(üstlüsayi))
toplist=[]

print("basamaklardaki sayılar :",basamak)

for i in basamak:
    toplist.append(int(i))
print(x," üzeri ",y," olan sayının basamakları toplamı :",sum(toplist))
