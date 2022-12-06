#check the 2 largest number
"""
a=int(input("Enter the value of a ="))
b=int(input("Enter the value of b ="))
c=int(input("Enter the value of c ="))
if a>b:
    big=a
else:
    a,b=b,a
    big=a
if b>a:
    big2=b
else:
    big2=c
if big>big2:
    print("big1",big)
    print("big2",big2)
else:
    print("big1",big2)
    print("big2",big)"""
n=input()
a=n[0]
b=n[1]
c=n[-1]
d=n[-2]
e=int(a)
f=int(b)
g=int(c)
h=int(d)
i=e+f
j=g+h
k=i*j
print("%d %d"%(i,j))
print(k)









