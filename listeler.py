liste1=["araba","kamyon",1234,223,5,2.5,"görkem","efe","emre"]

def liste_parser(liste):
    sayılar=[]
    isimler=[]
    for item in liste:
        if isinstance(item,int) or isinstance(item,float):
            sayılar.append(item)
        elif isinstance(item,str):
            isimler.append(item)
    return print("sayılar listesi:",sayılar,"\n","isimler listesi:",isimler)

liste_parser(liste1)