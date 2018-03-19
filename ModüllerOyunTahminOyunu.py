import random
import time

print("*****************************")
print("****SAYI TAHMİN OYUNU****")
print("*****************************")

rasgelesayi=random.randint(1,1000)
tahminhak=15
while True:
    tahmin=int(input("Sayı tahmin ediniz : "))

    if tahmin>rasgelesayi:
        print("bilgiler sorgulanıyor, bekleyiniz....")
        time.sleep(1)
        print("Daha küçük bir sayı tahmin ediniz.")
        tahminhak-=1
    elif tahmin<rasgelesayi:
        print("bilgiler sorgulanıyor, bekleyiniz....")
        time.sleep(1)
        print("Daha büyük bir sayı tahmin ediniz.")
        tahminhak -= 1
    else:
        print("bilgiler sorgulanıyor, bekleyiniz....")
        time.sleep(1)
        print("Tebrikler sayı doğru",rasgelesayi)
        break
    if tahminhak==0:
        print("Tahmin hakkınız doldu...")
        print("Game Over :) ")
        print("Doğru sayı : ",rasgelesayi)
