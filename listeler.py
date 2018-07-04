liste1=["araba","kamyon",1234,223,5,2.5,"görkem","efe","emre"]

def liste_parser(liste):
    sayılar=[]
    isimler=[]
    for item in liste:
        if type(item)==int or type(item)==float:
            sayılar.append(item)
        elif type(item)==str:
            isimler.append(item)
    return print("sayılar listesi:",sayılar,"\n","isimler listesi:",isimler)

liste_parser(liste1)