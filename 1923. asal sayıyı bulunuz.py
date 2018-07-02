
#"İlk 6 asal asal sayıyı listelersek(2, 3, 5, 7, 11 ve 13) 6. asal sayının 13 olduğunu görürüz.
#1923. asal sayıyı hesaplayan yazılımı python dilinde yazınız."


sayilist=[2,3,5,7]
for i in range(2,10000):
    if i%i==0 and i%1==0 and i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%6!=0 and i%7!=0 and i%8!=0 and i%9!=0:
        sayilist.append(i)
print("Sıfırdan başalayıp 1923. asal sayı : ",sayilist[1922])