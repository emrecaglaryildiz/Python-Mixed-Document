file=open("bilgiler.txt","w",encoding="utf-8")
file.write("emre çağlar")
file.close()

with open("bilgiler.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik=file.read(6)
    print(icerik)
    print(file.tell())


with open("bilgiler.txt", "r", encoding="utf-8") as file:
    file.seek(0)
    icerik2=file.read(4)
    print(icerik2)
    print(file.tell())
