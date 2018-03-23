try:
    a=int(input("birinci sayıyı giriniz :"))
    b=int(input("ikinci sayıyı giriniz :"))
    print("iki sayı bölümü : ",a/b)
except ValueError:
    print("Lütfen sayı giriniz...")
except ZeroDivisionError:
    print("bir sayı sıfıra bölünemez")
print("bloklar bitti.")
