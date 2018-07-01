class çalışan():
    def __init__(self,isim,maaş,departman):
        print("Çalışan sınıfı init fonksiyonu")
        self.isim=isim
        self.maaş=maaş
        self.departman=departman
    def bilgilerigöster(self):
        print("""Çalışan sınıfı özellikleri
        isim: {}
        maaş: {}
        departman: {}
        """.format(self.isim,self.maaş,self.departman))

class yönetici(çalışan): # Çalışan sınıfı özellikleri miras alınıyor ve aynen tek satırda tüm özellikler burada :)
    #pass
    def zam_yap(self,zam_miktarı):
        self.maaş+=zam_miktarı

emre = çalışan("emre",3000,"yazılım")
çağlar = çalışan("çağlar",2500,"yazılım")
yıldız = çalışan("yıldız",2000,"yazılım")

print(çalışan.bilgilerigöster(emre))
print(çalışan.bilgilerigöster(çağlar))
print(çalışan.bilgilerigöster(yıldız))

Yönetici=yönetici("EmreY",4500,"Bilişim")

print(yönetici.bilgilerigöster(Yönetici))