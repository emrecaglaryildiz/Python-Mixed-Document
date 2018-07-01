obj="elma"
print("\n1- birinci yöntem : print list ile elemanı bir liste içine alıp ayırır")
print(list(obj),"\n")
print("\n")
print("2- ikinci yöntem : for ile alt alta sıralayıp eleman içinde gezer")
for i in obj:
    print(i)
print("\n")
print("3- üçüncü yöntem : eleman üzerinde gezdikten sonra parçaları listeye toplayalım")
liste1=[]
for i in obj:
    liste1.append(i)
print(liste1)