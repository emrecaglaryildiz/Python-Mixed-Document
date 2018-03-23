def terscevir(s):
    if  type(s)!=str :
        raise ValueError("Lütfen string değer gir...")
    else:
        return s[::-1]

print(terscevir("emre"))

print(terscevir(123))
