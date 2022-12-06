for x in range (1,10001):
    dc=0
    for a in range (1,11):
        if x%a==0:
            dc=dc+1
        if dc==10:
            print(x)

"""import random as r 
l=[]
for a in range (5):
    x=r.randint(10,20)
    l.append(x)"""
