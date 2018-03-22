from bs4 import BeautifulSoup
import requests  #request kütüphanesini içeri aktardım.

source1 = requests.get('https://kur.doviz.com/serbest-piyasa/amerikan-dolari') #get fonksiyonu ile request gönderdik.
source2 = requests.get('https://kur.doviz.com/serbest-piyasa/amerikan-dolari')
source3 = requests.get('https://kur.doviz.com/serbest-piyasa/euro')

soup1 = BeautifulSoup(source1.text, 'html.parser')
soup2 = BeautifulSoup(source2.text, 'html.parser')
soup3 = BeautifulSoup(source3.text, 'html.parser')

link=soup1.find('span', attrs={'class':'menu-row2'})
link1=soup2.find('span', attrs={'class':'color-green'})
link2=soup3.find('span', attrs={'class':'color-green'})

print("---------------------------------")
print("Gram Altın fiyatı : "+link.text)
print("---------------------------------")
print("Dolar fiyatı      : "+link1.text)
print("---------------------------------")
print("Euro fiyatı       : "+link2.text)
print("---------------------------------")

i=input("çıkmak için bir tuşa basınız...")
