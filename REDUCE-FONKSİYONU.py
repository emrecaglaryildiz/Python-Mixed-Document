from _functools import reduce

"""
************************
Reduce fonksiyonu örnek 1 
************************
"""

def maksimum(x, y):
    if x > y:
        return x
    else:
        return y
List1 = [1, 5, 7, 9]
z = reduce(maksimum, List1)
print(z)

"""
************************
Reduce fonksiyonu örnek 2 
************************
"""

def toplama(z,t):
    return z+t
list2 = [1, 5, 7, 9]
t = reduce(toplama, list2)
print(t)