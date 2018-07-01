#0 ile 100 arasında rastgele sayı üretip, kullanıcının bu sayıyı tahmin etmesini isteyen ve kaç tahmin sonunda sayıyı bulduğunu kullanıcıya gösteren yazılımı python dilinde kodlayınız.

import random

sayaç=0
sayı=random.randint(1,1000)

tahminler = []
while sayaç<20:
    tahmin = int(input("Tahmin ettiğiniz sayı nedir? :"))


    if  sayı>tahmin:
        print("Tahmin sayınızı yükseltiniz...")
        tahminler.append(tahmin)
        sayaç += 1
        kalanhak = 20 - sayaç
        print("Kalan tahmin hakkınız : ", kalanhak)
    elif sayı<tahmin:
        print("Tahmin sayısınızı düşürünüz...")
        tahminler.append(tahmin)
        sayaç += 1
        kalanhak = 20 - sayaç
        print("Kalan tahmin hakkınız : ", kalanhak)
    else:
        tahminler.append(tahmin)
        print("\n********Tebrikler, Doğru tahmin.********\n")
        print("********************************")
        print("/*/*/*/*/Yapılan Tahmin sayısı :",len(tahminler),"\*\*\*\*\*")
        print("********************************")
        print("/*/*/*/*/ Tahmin ettiğiniz sayılar : ",tahminler,"\*\*\*\*\*")
        print("********************************")
        break