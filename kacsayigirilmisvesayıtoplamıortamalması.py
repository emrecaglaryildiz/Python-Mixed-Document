a=[]
x=input("kaç adet sayı girişi yapacaksın : ")
x=int(x)
while x>0:
    num=int(input("sayı giriniz :"))
    a.append(num)
    x = x - 1
al=len(a)
at=sum(a)
print("girdiğiniz sayılar : ",a)
print("girdiğiniz sayıların değerleri toplamının ortalaması : ",at/al)
