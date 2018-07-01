#2 veya 3'e tam bölünebilen 10000'dan küçük kaç adet sayı olduğunu bulan yazılımı python dilinde yazınız.

k=[]
for i in range(1,10000):
    if i%2==0 and i%3:
        k.append(i)
print(k)