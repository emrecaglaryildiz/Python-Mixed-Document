#Klavyeden girilen iki sayıyı çarpma operatörü (*)  kullanmadan çarpan yazılımı python dilinde kodlayınız.

def carpma(sayi1,sayi2):
    sonuc=0
    sayac=0
    while sayac<=sayi1:

        sonuc=sonuc+sayi2
        sayac+=1
    return sonuc

a=int(input("çarpılacak birinci sayıyı giriniz :"))
b=int(input("çarpılacak ikinci sayıyı giriniz :"))


print(carpma(a,b))