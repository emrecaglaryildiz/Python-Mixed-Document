# Aradaki sayıları tespit etme ------------------------------------------
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
#-------------------------------------------------------------------------

# Faktöriyel Bulma Fonksiyonu-------------------------------------------------------

def fakt (sayi):
    z = []
    fak = 1
    z.append(sayi)

    while sayi > 1:
        y = sayi - 1
        z.append(y)
        sayi = y

    for i in z:
        fak = fak * i

    return fak

#-------------------------------------------------------------------------

# Aradaki değerlerin faktöriyel değerlerinin hesabı ve listelenmesi ------

faktlist=[]

for i in c:
    faktlist.append(fakt(i))

print("aradaki sayılar : ", c)
print("aradaki sayıların faktöriyel değerleri : ", faktlist)
#---------------------------------------------------------------------------