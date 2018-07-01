#1 ile 5000 arasındaki tek sayıların ve çift sayıların toplamını ayrı ayrı hesaplayıp, ekrana yazdıran yazılımını python dilinde yazınız.

ts=[]
cs=[]
for i in range(1,5000):
    if i%2==0:
        cs.append(i)
    else:
        ts.append(i)
print("tek sayılar toplamı : ",sum(ts))
print("çift sayılar toplamı : ",sum(cs))