"""
Map kullanımı ve basit örnekler 1
"""

def çarp (x):
    return x*2
slist=[1,2,3,4,5,6]
y=list(map(çarp, slist))
print(y)

"""
Map kullanımı ve basit örnekler 2
"""

list1=[1,2,3,4,5]
list2=[5,3,7,9,2]
list3=[9,8,6,5,4]
lm1=list(map(lambda x,y,z: x*y*z, list1,list2,list3))
print(lm1)