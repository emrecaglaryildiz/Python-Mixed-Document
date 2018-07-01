sayi=int(input("n'e kadar kendi üstüyle toplanacak sayı giriniz :"))
listem=[]
for m in range(1,(sayi+1)):
    listem.append(m)
toplist=[]
for i in listem:
    i=i**i
    toplist.append(i)
print("sırasıyla kendiyle aynı kuvvete sahip sayılar :",toplist)
print("listedeki sayıların toplam değeri :",sum(toplist))


