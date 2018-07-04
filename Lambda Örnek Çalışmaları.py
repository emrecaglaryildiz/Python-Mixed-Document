# Normal fonksiyon kullanımı

#def kullanım :
def toplama(a,b):
    return a+b
print("def ile fonksiyon yazdık",toplama(3,4))

def toplama2(a,b,c): #over writing
    return a+b+c
print("def ile fonksiyon yazdık",toplama2(5,6,7))

#lambda Kullanım :
topla=lambda a,b:a+b
topla2=lambda a,b,c:a+b+c #over writing
print("lambda ile fonksiyon yazdık",topla(3,4))
print("lambda ile fonksiyon yazdık",topla2(5,6,7))

