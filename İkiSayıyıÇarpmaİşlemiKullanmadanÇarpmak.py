def çarpma(a,b):
    sayaç=0
    sonuc=0
    while sayaç<a:
        sonuc+=b
        sayaç+=1
    return sonuc

a=input("Çarpılacak ilk sayıyı giriniz : ")
b=input("Çarpılacak ikinci sayıyı giriniz : ")

print(çarpma(int(a),int(b)))