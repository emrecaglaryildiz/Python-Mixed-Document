sayaç=0
kişiler=[]
while sayaç<5:
    metin="""Merhaba {0}, bugün python çalışıyoruz. Kolay gelsin."""
    kişi=input("adın nedir? \n")
    kişiler.append(kişi)
    print(metin.format(kişi))

    sayaç+=1
    if sayaç==5:
        print(" \n-","Kursa katılan kişi sayısı : {0}".format(len(kişiler)))
        print("+","Kurs Kişi listesi","+")
        for i in kişiler:

            print(i)