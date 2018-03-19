#Kullanıcdan sayı alınız ve alınan sayıları kullanıcı çıkış yapınca göster.

sayılar=[]
while True :
    print("""Çıkış için 'q'ya basınız""")
    sayı=input("Sayı giriniz : ")
    sayılar.append(sayı)
    if sayı=="q":
        print("Sistemden çıkılıyor...")
        print("Grimiş olduğunuz sayılar aşağıdaki gibidir.")
        print(sayılar)
        break
