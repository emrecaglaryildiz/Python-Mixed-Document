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
print("aradaki sayılar : ", c)

f=[]
for i in c:
    y=i**2
    f.append(y)
print("aradaki sayılar kareleri : ", f)