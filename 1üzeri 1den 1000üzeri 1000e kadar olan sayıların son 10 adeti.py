#11 + 22 + 33 + ... + 10001000 işleminden elde edilen sayının son 10 rakamını hesaplayan yazılımı python dilinde yazınız.

listem=[]
for m in range(1,1001):
    listem.append(m)
toplist=[]
for i in listem:
    i=i**i
    toplist.append(i)
a=list(str(sum(toplist)))
b=a[-10:]
print("1'den 1000'e kadar olan aynı üste sahip sayılar toplamının son 10 hanesi",b)