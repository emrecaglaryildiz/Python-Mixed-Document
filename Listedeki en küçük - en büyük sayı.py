
liste=[1,2,3,4,5,45,76,98,91,18]

print("listedeki değeri en küçük sayı",min(liste)) # listedeki değeri en küçük sayı
print("listedeki değeri en büyük sayı",max(liste)) # listedeki değeri en büyük sayı

# Liste değerlerinden ortadaki olanı :)
liste.sort()
print("listedeki değerlerin ortasındaki sayı :",liste[int(len(liste)/2)])