c=[]
a=int(input("1.sayıyı giriniz : "))
b=int(input("2.sayıyı giriniz : "))

if a<b:
    while a<b:
        d = a + 1
        c.append(d)
        a=d
else:
    while b<a:
        ey = b+1
        c.append(ey)
        b = ey

c.pop(-1)
print("iki sayı arasında bulunan sayılar : ", c)

z=[]

for i in c:
    if i%7==0:
        z.append(i)
print("iki sayı arasındaki sayılardan 7'nin katı olanlar : ",z)
