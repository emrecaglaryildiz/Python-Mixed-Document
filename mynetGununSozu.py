from bs4 import BeautifulSoup
import requests 
source = requests.get('https://www.mynet.com') 
# print(source.text) # .text sayfanın kaynak kodlarını yazdırmamıza yarıyor. 
#print(source.content) diyerek de ulaşabiliriz.
soup = BeautifulSoup(source.text, 'html.parser')
basliklar = soup.findAll('p', attrs={'class':'word-of-day-text'})
# print(basliklar)
for i in basliklar:
    print(i.text)
i=input("çıkmak için bir tuşa basınız...")
