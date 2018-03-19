#Bir sayının mükemmel olup olmadığını bulun.

sayı=int(input("Sayı giriniz :"))
i=1
toplam=0
while i>sayı:
    if sayı%i:
        toplam+=i
        i+=i
if  toplam==sayı:
    print("sayı mükemmeldir.")
else:
    print("sayı mükemmel değildir.")