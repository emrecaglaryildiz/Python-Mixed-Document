#k > 0 olmak şartıyla (k-1) sayısı 4’e tam bölünüyorsa hilbert sayısı olarak adlandırılır.
#Örnek: 9 sayısının 1 ekseği olan 8 sayısı 4'e tam bölündüğü için 9 sayısı hilbert sayıdır.
#1000'den küçük tüm hilbert sayılarını listeleyen yazılımı python dilinde yazınız.
hilbert=[]
for i in range(1,1000):
    if (i-1)%4==0 :
        hilbert.append(i)
print("1000'den küçük tüm hilbert sayıları listesi : ",hilbert)
print("1000'den küçük hilbert sayısı : ",len(hilbert)," tanedir.")