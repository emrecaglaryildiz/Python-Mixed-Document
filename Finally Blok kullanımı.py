#Finally Blok kullanımı

try:
    a=int(input("birinci sayıyı giriniz :"))
    b=int(input("ikinci sayıyı giriniz :"))
    print("iki sayı bölümü : ",a/b)
except ValueError:
    print("Lütfen sayı giriniz...")
except ZeroDivisionError:
    print("bir sayı sıfıra bölünemez")
finally:  #except e girsede girmesede kesin çalışması gereken kodları yaz.
    print("finally çalıştı.")
print("bloklar bitti.")
