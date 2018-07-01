#3'ün veya 5'in 1000'den küçük tüm katlarının toplamını hesaplayan yazılımı python dilinde programlayınız

bölünenler=[]
for i in range(1,1000):
    if i%3 or i%5:
        bölünenler.append(i)
print(sum(bölünenler))
