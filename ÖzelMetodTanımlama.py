class Kitap():
    pass

# kitap=Kitap() #__init__ kendisini çağırıyor.

# print(kitap)

class Kitap():
    def __init__(self,isim,yazar,sayfa_sayısı,tür):
        print("init çalıştı")
        self.isim=isim
        self.yazar=yazar
        self.sayfa_sayısı=sayfa_sayısı
        self.tür=tür
    def __str__(self): # istenen string değer verilmesi için ayarlanabilir.
        return "İsim:{}\nYazar:{}\nSayfa Sayısı:{}\nTür:{}".format(self.isim,self.yazar,self.sayfa_sayısı,self.tür)
    def __len__(self): #istene sayısal değer gösterilebilri.
        return self.sayfa_sayısı

kitap=Kitap("İstanbul Hatırası","Ahmet Ümit",561,"Polisiye")

print(kitap)

print(len(kitap))

