# Armstrong sayısı bulma programı

sayı=input("Sayı giriniz : ")
bas_say_deg=len(sayı)
basamak=0
toplam=0
sayı=int(sayı)
gecici_sayı=sayı

while gecici_sayı>0:
    basamak=gecici_sayı%10
    toplam+=(basamak**bas_say_deg)
    gecici_sayı//=10
if toplam==sayı:
    print("Sayı Armstrong sayısıdır.")
else:
    print("Sayı armstrong sayısı değildir...")