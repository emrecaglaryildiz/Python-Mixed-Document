print("*************************")
print("Kullanıcı Giriş Ekranı")
print("*************************")

kadi="emre"
sifre="47556"
girishak=3

while True:
    kullanıcı_adi=input("Kullanıcı : ")
    parola=input("Parola : ")
    if (kadi!=kullanıcı_adi and sifre==parola):
        print("kullanıcı adı hatalı")
        girishak-=1
    elif (kadi==kullanıcı_adi and sifre!=parola):
        print("şifre hatalı")
        girishak -= 1
    elif (kadi!=kullanıcı_adi and sifre!=parola):
        print("kullanıcı adı - şifre hatalı")
        girishak -= 1
    else:
        print("sisteme giriş yapıldı")
        break
    if (girishak==0):
        print("Giriş hakkınız bitti !! ")
        break