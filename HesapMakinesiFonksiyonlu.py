# This function adds two numbers / toplama fonksiyonu
def toplama(x, y):
   return x + y

# This function subtracts two numbers / Çıkarma fonksiyonu
def çıkarma(x, y):
   return x - y

# This function multiplies two numbers / Çarpma  fonksiyonu
def çarpma(x, y):
   return x * y

# This function divides two numbers / bölme fonksiyonu
def bölme(x, y):
   return x / y

print("İşlemler :")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")

# Take input from the user / Kullanıcıdan işlem alınır
işlem = input("İşlem seçiniz (1/2/3/4):")

num1 = int(input("İlk sayıyı giriniz : "))
num2 = int(input("Son sayıyı giriniz : "))

if işlem == '1':
   print(num1,"+",num2,"=", toplama(num1,num2))

elif işlem == '2':
   print(num1,"-",num2,"=", çıkarma(num1,num2))

elif işlem == '3':
   print(num1,"*",num2,"=", çarpma(num1,num2))

elif işlem == '4':
   print(num1,"/",num2,"=", bölme(num1,num2))
else:
   print("Hatalı Giriş")