sayilist=[2,3,5,7]
for i in range(2,1000):
    if i%i==0 and i%1==0 and i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%6!=0 and i%7!=0 and i%8!=0 and i%9!=0:
        sayilist.append(i)
print(sum(sayilist))