#Dosya açma için aşağıdaki gibi komutla şuan bulunan konuma dosya açabilirsiniz.

file=open("C:/Users/Emre YILDIZ/Desktop/deneme1.txt","w",encoding="utf-8") #Türkçe karakter için utf8 ile encoding yapmak gerek.
file.write("Emre YILDIZ\nÇAĞLAR YILDIZ\nEmre Çağlar YILDIZ ")
file.close()
file=open("C:/Users/Emre YILDIZ/Desktop/deneme1.txt","a",encoding="utf-8")
file.write("\nMerhaba Dostlar")
file.close()
file=open("C:/Users/Emre YILDIZ/Desktop/deneme1.txt","r",encoding="utf-8")

for i in file:  # Dosya içini okumak için "for" döngüsü kullanılabilir.
    print(i, end="")  # For dosyayı basarken boşluk bırakmasın istersek end ile sorunu çözebiliriz.
file.close()
