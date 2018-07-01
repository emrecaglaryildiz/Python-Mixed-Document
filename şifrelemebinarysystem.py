harfler = ['a', 'b', 'c', 'ç', 'd', 'e', 'f', 'g', 'h', 'i', 'ı', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's',
           'ş', 'i',
           't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z', ' ', '?', '.', ',', ':', ';', '!', '0', '1', '2', '3', '4', '5', '6',
           '7', '8', '9']


def Binary(sayi):
    binary_system = [128, 64, 32, 16, 8, 4, 2, 1]
    binary = ''
    for x in binary_system:
        if sayi >= x:
            binary += '1'
            sayi -= x
        else:
            binary += '0'
    return binary


def Sifrele(metin):
    sayac = 0
    sifreli_metin = ''
    for x in metin.lower():
        sayac = 0
        for y in harfler:
            sayac += 1
            if x == y:
                myCode = Binary(sayac)
                sifreli_metin += myCode
                break
    return sifreli_metin


def SifreCoz(sifre):
    sayac = 0
    toplam = 0
    sekiz_adim = ''
    sifresiz_metin = ''
    for x in sifre:
        sekiz_adim += x
        if len(sekiz_adim) == 8:
            binary_system = [128, 64, 32, 16, 8, 4, 2, 1]
            for y in sekiz_adim:
                if y == '1':
                    toplam += binary_system[sayac]
                else:
                    toplam += 0
                sayac += 1

            sifresiz_metin += harfler[toplam - 1]
            sekiz_adim = ''
            sayac = 0
            toplam = 0
    return sifresiz_metin


while True:
    metin = input('Şifrelenecek Metni Girin : ')
    pw = Sifrele(metin)
    print(pw)

    sifre = input('Şifresi Çözülecek Metin : ')

    mtn = SifreCoz(sifre)
    print(mtn)