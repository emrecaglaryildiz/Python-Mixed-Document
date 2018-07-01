import sys
def Sifrele():
    sgiris = input("Şifrelemek için bir anahtar sözcüğü giriniz(enaz 5, enfazla 15 karakter): ")
    if(len(list(sgiris))<5 or len(list(sgiris))>15):
        print("Lütfen kurallara riayet edin")
    else:
        yol = input("Şifrelenecek metin dosyasının tam yolunu giriniz: \n")
        dosya = open(yol, "r")
        veri = dosya.read()
        veri = list(veri)
        sgiris = list(sgiris)
        say=0
        for i in sgiris:
            arasonuc = ""
            for l in veri:
                sonuc = ord(l)+ord(i)
                if(sonuc >= 127):
                    sonuc = sonuc % 127
                arasonuc += chr(sonuc)
        dosya = open("sifrelidosya.txt", "a")
        dosya.write(arasonuc)
        dosya.close()
def Coz():
    sgiris = input("Şifre Çözmek için bir anahtar sözcüğü giriniz(enaz 5, enfazla 15 karakter): ")
    if(len(sgiris)<5 or len(sgiris)>15):
        print("Lütfen kurallara riayet edin")
    else:
        dosya = open("sifrelidosya.txt", "r")
        veri = dosya.read()
        veri = list(veri)
        sgiris = list(sgiris)
        gelen = ""
        dosya.close()
        say=0
        for i in sgiris:
            arasonuc = ""
            for l in veri:
                sonuc = ord(l) - ord(i)
                if(sonuc<=0):
                    sonuc = sonuc + 127
                arasonuc += chr(sonuc)
        dosya = open("cozulmusdosya.txt", "a")
        dosya.write(arasonuc)
        dosya.close()
        print("\nSifresi çözülmüş metin: ", arasonuc,"\n")
while(True):
    giris = input("Hangi İşlemi yapmak istiyorsunuz? \nSifrele: Metin dosyası şifreler\nCoz: Metin dosyası şifre çözer\nx: Çıkış\n")
    if(giris == "Sifrele"):
        Sifrele()
    if(giris == "Coz"):
        Coz()
    if(giris == "x"):
        sys.exit(0)