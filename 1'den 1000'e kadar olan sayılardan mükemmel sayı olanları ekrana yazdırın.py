#1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.
#Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6).

def mukemmelsayıbulma():
    sayı=range(1,100)
    i=1
    toplam=0
    while i>sayı:
        if sayı%i:
            toplam+=i
            i+=i
    if  toplam==sayı:
        return True
    else:
        return False

sayılar=[]
for i in range(1,1000):
    if ((mukemmelsayıbulma(i))==True):
        sayılar.append(i)
print(sayılar)
