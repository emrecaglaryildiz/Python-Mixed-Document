# Stringler içinden sadece sayıları bulan bir program yapma

liste=["435","emre","i7","19","ahmet"]
for i in liste:
    try:
        i=int(i)
        print(i)
    except:
        pass
