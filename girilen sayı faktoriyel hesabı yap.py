z=[]
fak=1

x=int(input("Faktoriyel öğrenilmek istenen sayı giriniz : "))
z.append(x)

while x>1:
    y=x-1
    z.append(y)
    x=y

for i in z:
    fak=fak*i

print("faktöriyel : ",fak)