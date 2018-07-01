#Klavyeden girilecek n sayısı için 1üzeri1+2üzeri2+3üzeri3+…..nüzerin değerini hesaplayan yazılımı python dilinde yazınız.

a=int(input("bir sayı giriniz : "))
liste=[]

for i in range(1,a):
    for m in range(1,a):
        x=m**i
        liste.append(x)
print(sum(liste))