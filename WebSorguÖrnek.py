import requests
from bs4 import BeautifulSoup
liste=[]
url="https://detect.mobiliz.com.tr/"
r=requests.get(url)
soup=BeautifulSoup(r.content,"html.parser")
for kelimegruplari in soup.find_all("tbody"):
    içerik=kelimegruplari.text
    print(içerik)
