alfabe=["a","b","c","ç","d","e","f","g","ğ","h","ı","i","j","k","l","m","n","o","ö","p","r","s","ş","t","u","ü","v","y","z"]
a=input("Sırasını öğrenmek istediğiniz harfi küçük olarak tuşlayınız : ")

for x in alfabe:
    if x==alfabe:
        print((alfabe.index(x))+1)
