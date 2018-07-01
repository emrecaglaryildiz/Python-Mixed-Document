import sys

def uc():
    for x in range(0, 6, +1):
        print(x * "*")

def kare():
    for i in range(3):
        print('*' * 5)

def dikdortgen():
    for i in range(3):
        print('*' * 10)

def baklava():
    k = 0
    for i in range(1, 7):
        for l in range(1, (6 - i) + 1):
            print(end="  ")
        while k != (2 * i - 1):
            print("* ", end="")
            k = k + 1
        k = 0
        print()
    k = 0
    for i in range(6, 0, -1):
        for l in range((5 - i) + 1, 0, -1):
            print(end="  ")
        while k != (2 * i - 1):
            print("* ", end="")
            k = k + 1
        k = 0
        print()

def paralelkenar():
    islem = ""
    for i in range(4):
        for l in range(8):
            islem = l * "*"
        print(' ' * i, islem)

def cem(alan, ch='*'):
    xs = 4.2
    genislik = 3 + int(0.5 + xs * alan)

    alan2 = alan ** 2
    for y in range(-alan, alan + 1):
        x = int(0.5 + xs * (alan2 - y ** 2) ** 0.5)
        s = ch * x
        print(s.center(genislik))

while (True):
    giris = input("Çizilmesi istenen nesneyi giriniz(kare,dikdortgen,ucgen,baklava,cember,pkenar):\n")
    if (giris == "kare"):
        kare()
    if (giris == "dikdortgen"):
        dikdortgen()
    if (giris == "ucgen"):
        uc()
    if (giris == "baklava"):
        baklava()
    if (giris == "pkenar"):
        paralelkenar()
    if (giris == "cember"):
        for i in range(4, 5):
            cem(i, '*')
    if (giris == "x"):
        sys.exit(0)