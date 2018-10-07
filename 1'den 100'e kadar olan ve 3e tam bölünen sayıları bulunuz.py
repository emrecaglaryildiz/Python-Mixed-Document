#1'den 100'e kadar olan ve 3e tam bölünen sayıları bulunuz ?

sayılar=[]
for i in range(1,100):
    if (i%3==0):
        sayılar.append(i)
print(sayılar)

