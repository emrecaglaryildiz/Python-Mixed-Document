def yuzyil(n):
    return int((n/100)+1)

yil=input("hangi yılın yüzyılını öğrenmek istersin ? :")
x=yuzyil(int(yil))

if 1<x<=2018:
    print("sorguladığınız yılın yüz yılı : ",x)
else:
    print("Seçtiğiniz tarih aralığını kontrol ediniz...")