#Fibonacci serinin 15 rakamından çift sayılarının toplamını hesaplayan yazılımı python dilinde yazınız.

a=1
b=1
listem1=[]
listem2=[]

for i in range(0,15):
    a,b=b,a+b
    listem1.append(b)
print("/////////////////////////////////////////////////////////////")
print("1-) ilk 15 adet fibonacci sayısı :\n",listem1)

for m in listem1:
    if m%2==0:
        listem2.append(m)
print("/////////////////////////////////////////////////////////////")
print("2-) ilk 15 adet fibonacci sayısından 2'ye bölünenler :\n",listem2,)
print("/////////////////////////////////////////////////////////////")
print("3-) ilk 15 adet fibonacci sayısından 2'ye bölünen sayılar toplamı :\n",sum(listem2))
print("/////////////////////////////////////////////////////////////")