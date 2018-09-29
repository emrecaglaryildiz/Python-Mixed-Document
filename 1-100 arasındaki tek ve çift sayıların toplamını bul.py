a=[]
b=[]
for i in range(0,100):
    if i%2==0:
        a.append(i)
    else:
        b.append(i)
print("1-100 Çift sayılar ",a)
print("1-100 Çift sayıların toplamı : ", sum(a))

print("1-100 Tek sayılar ",b)
print("1-100 Tek sayıların toplamı : ", sum(b))

