#!/usr/bin/env python3.0


kim=input("senin adın ne\n")
print("Merhaba "+ kim +" sisteme hoşgeldiniz !")

a="çık"
b="sipariş vereceğim"
c="iş başvurusu yapacağım"

soru=input("size nasıl yardımcı olabilirim \n" +a+" ? - 1 \n" +b+" ? - 2 \n"+c+" ? - 3 \n")

if(soru=="1"):
    exit()
elif(soru=="2"):
    a="Yiyecek "
    b="İçecek "
    tercih=input("Ne arzu edersiniz" +" \n"+"1- "+a+" \n"+"2- "+b+" \n")
    if(tercih=="2"):
                b1="kola"
                b2="fanta"
                b3="sprite"
                seçim=input("1- "+b1+" \n"+"2- "+b2+" \n"+"3- "+b3+" \n")
    if(seçim=="1"):
                            print("siparişiniz alınmıştır.")
                            input()
    elif(seçim=="2"):
                            print("siparişiniz alınmıştır.")
                            input()
    elif(seçim=="3"):
                            print("siparişiniz alınmıştır.")
                            input()
elif(soru=="3"):
    print("devam edecek menü yoktur, yazılımı geliştiriniz :)")

