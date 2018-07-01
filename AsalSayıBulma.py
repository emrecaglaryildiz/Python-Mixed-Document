def asal_mi(sayi):
    if sayi==1:
        return False
    elif sayi==2:
        return True
    else:
        for i in range(2,sayi):
            if sayi%i==0:
                return False
            return True

while True:

    sayi1=input("sayı giriniz : ")

    if (sayi1=="q"):
        break

    else:
        sayi1=int(sayi1)
        if (asal_mi(sayi1)):
            print(sayi1,"asal bir sayıdır.")

        else:
            print(sayi1,"asal bir sayı değildir.")

