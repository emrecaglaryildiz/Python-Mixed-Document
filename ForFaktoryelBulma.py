print("""***********************
***********************
Faktöriyel Bulma Programı
***********************
çıkmak için "q" basınız
***********************""")

while True:
    sayi=input("Bir sayı giriniz : ")
    if (sayi=="q"):
        print("Çıkış yapılıyor...")
        break
    else :
        sayi=int(sayi)
        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel*=i
        print("Faktoriyel = ",faktoriyel)
