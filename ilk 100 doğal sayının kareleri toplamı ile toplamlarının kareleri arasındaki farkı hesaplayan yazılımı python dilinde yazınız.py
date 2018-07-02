#ilk 100 doğal sayının kareleri toplamı ile toplamlarının kareleri arasındaki farkı hesaplayan yazılımı python dilinde yazınız

karetoplistem=[]
for i in range(1,100):
    i=i**2
    karetoplistem.append(i)

toplamatoplistem=[]
for m in range(0,100):
    m=m+1
    toplamatoplistem.append(m)

print("sayıların tek tek kareleri toplamı : ",sum(karetoplistem))
print("sayılar toplamının karesi : ",sum(toplamatoplistem)**2)

print("1'den 100'e kadar sayıların kareleri toplamı ile toplamları karesi farkı :",sum(karetoplistem)-(sum(toplamatoplistem)**2))

