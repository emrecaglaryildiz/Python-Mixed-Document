print("***************************************")
print("X BANK ATM - HOŞGELDİNİZ")
print("X BANK ATM - BAKİYE SORMA 1")
print("X BANK ATM - PARA YATIRMA 2")
print("X BANK ATM - PARA ÇEKME 3")
print("X BANK ATM - ÇIKIŞ için 'q' ya basınız")
print("***************************************")

bakiye=2000

while True:
    işlem= input("işlem seçiniz : ")
    if (işlem=="q"):
        print("İşlem sonlandırlıyor...")
        print("Yine bekleriz")
        break
    elif (işlem=="1"):
        print("{} tl bakiyeniz bulunmaktadır.".format(bakiye))
        print("Yine bekleriz")
        break

    elif (işlem == "2"):
        yatantutar=int(input("Yatırmak istediğiniz tutar giriniz :"))
        bakiye+=yatantutar
        print("Yatırılan tutar : {}".format(yatantutar))
        print("Toplam bakiyeniz {}".format(bakiye))
        print("Yine bekleriz")
        break

    elif (işlem == "3"):
        çekilentutar = int(input("Çekmek istediğiniz tutar giriniz :"))
        if ((bakiye - çekilentutar)<0):
            print("Bakiyeniz yetersizdir. Bakiyenize uygun işlem yapınız...")
            continue
        bakiye-=çekilentutar
        print("Çekilen tutar : {}".format(çekilentutar))
        print("Toplam bakiyeniz {}".format(bakiye))
        print("Yine bekleriz")
        break

    else:
        print("hatalı seçim")
        print("Tekrar işlem seçiniz")