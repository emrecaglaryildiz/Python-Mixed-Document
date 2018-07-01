import random
import time

class Kumanda():

    def __init__(self,tv_durum="kapalı",tv_ses=0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum=tv_durum
        self.tv_ses=tv_ses
        self.kanal_listesi= kanal_listesi
        self.kanal=kanal

    def tv_ac(self):
        if (self.tv_durum=="Açık"):
            print("Tv zaten Açık")
        else:
            print("Tv Açılıyor...")
            time.sleep(1)
            print("Tv Açıldı...")
            self.tv_durum="Açık"

    def tv_kapat(self):
        if (self.tv_durum=="Kapalı"):
            print("Tv zaten kapalı")
        else:
            print("Tv Kapanıyor...")
            print("Tv Kapandı...")
            self.tv_durum="Kapalı"

    def ses_ayarları(self):
        while True:
            cevap=input("Sesi Azalt: '<'\nSesi Artır:'>'\nÇıkış: 'q' basınız")

            if  (cevap=="<"):
                if  (self.tv_ses!=0):
                   self.tv_ses-=1
                   print("Ses :",self.tv_ses)

            elif (cevap==">"):
                if (self.tv_ses!=40):
                    self.tv_ses+=1
                    print("Ses :",self.tv_ses)

            else:
                print("Ses Güncellendi: ",self.tv_ses)
                break

    def kanal_ekle(self,Kanal_isim):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(Kanal_isim)
        print("Kanal Eklendi...")

    def rasgele(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        self.kanal=self.kanal_listesi[rastgele]
        print("Şu anki Kanal: ",self.kanal)

    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return "Tv Durum: {}\nTv Ses: {}\nKanal Listesi: {}\nŞu anki kanal: {}\n.".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)


kumanda=Kumanda()
print(""""
    
    Televizyon Uygulaması
    
    1.Tv Aç
    2.Tv Kapat
    3.Tv Ses Ayarları
    4.Kanal Ekle
    5.Kanal Sayısı Öğrenme
    6.Rastgele Kanal Geçme
    7.Tv Bilgileri
    
    Çıkmak için 'q' basınız...
    """)

while True:
        işlem=input("İşlem giriniz : ")
        if işlem=="q":
            print("Çıkış yapılıyor...")
            time.sleep(1)
            break
        elif işlem=="1":
            kumanda.tv_ac()
        elif işlem=="2":
            kumanda.tv_kapat()
        elif işlem=="3":
            kumanda.ses_ayarları()
        elif işlem=="4":
            kanal_isimleri=input("Kanal isimlerini ',' ile ayırarak yazınız...")
            kanal_listesi=kanal_isimleri.split(",")
            for eklenecekler in kanal_listesi:
                kumanda.kanal_ekle(eklenecekler)
        elif işlem=="5":
            print("Kanal sayısı :", len(kumanda))
        elif işlem=="6":
            kumanda.rasgele()
        elif işlem=="7":
            print(kumanda)
        else:
            print("Geçersiz işlem...")










