
class yazılımcı() :
    def __init__(self, isim,soyad,numara,maaş,diller):
        self.isim=isim
        self.soyad=soyad
        self.numara=numara
        self.maaş=maaş
        self.diller=diller
    def bilgilerigöster(self):
        print("""
        Yazılımcı Objesi özellikleri
        İsim: {}
        Soyad: {}
        Numara: {}
        Maaş: {}
        Bildiği Diller : {}
        """.format(self.isim,self.soyad,self.numara,self.maaş,self.diller))


#İlk önce oluşturulacak objeyi sonrasında sınıfı gir, bilgi ekle.
Yazılımcı=yazılımcı("emre","yıldız",12345,3000,["c#","java","python"])
Yazılımcı.bilgilerigöster()