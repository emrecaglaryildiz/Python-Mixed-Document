class Bilgisayar():
    def __init__(self,cpu,ram,ekran_kartı,os,fiyat):
        self.cpu=cpu
        self.ram=ram
        self.ekran_kartı=ekran_kartı
        self.os=os
        self.fiyat=fiyat

    def __str__(self):
        print("""PC Özellikleri
        Cpu : {}
        Ram : {}
        Ekran kartı : {}
        İşletim sistemi : {}
        Fiyat : {}
        """.format(self.cpu,self.ram,self.ekran_kartı,self.os,self.fiyat))


    def ram_ugrade(self,ram_upgrade):
        self.ram+=int(ram_upgrade)
        print("Ram yükseltildi. Yenisi : {} ".format(self.ram))

    def ekran_kartı_upgrade(self,ekran_kartı_upgrade):
        self.ekran_kartı+=ekran_kartı_upgrade
        print("Ekran kartı yükseltildi. Yenisi : {}".format(self.ekran_kartı))

    def os_change(self,os_change):
        self.os=os_change

pc=Bilgisayar('i7',8,4,'win','6875TL')
pc.ram_ugrade(1)
pc.ekran_kartı_upgrade(2)
print(pc)