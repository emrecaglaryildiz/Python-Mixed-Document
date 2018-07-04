liste=[1,2,4,5,6,"a","b","c"]

#listeye eleman ekleme
liste.append("d")

#Listeyi küçükten büyüğe sıralar
#liste.sort()

#listeyi tersten büyükten küçüğe sıralar
liste.reverse()

#listeden istenilen elemanı çıkartır
liste.remove("c")

#listede sayma işlemi yapar
liste.count("a")

#listede verilen indexteki veriyi siler ve ekranda silineni gösterir
liste.pop(2)

#listede kopyalama işlemlerinde kullanılır
liste.copy()

#verilen liste elemanının index değerini verir
liste.index("d")

#verilen str değeri karakterlerine parçalayarak liste sonuna ekler
liste.extend("emre")

#listenin istenilen indexine eleman ekler
liste.insert(5,7)

#listeyi temizleme
#liste.clear()

print(liste)