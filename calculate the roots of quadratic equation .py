import math as m 
a=int(input("Enter the value of a ="))
b=int(input("Enter the value of b ="))
c=int(input("Enter the value of c ="))
d=b*b-4*a*c
if d>0:
    print("Roots are real")
    r1= (-b+m.sqrt(d))/(2*a) 
    r2= (-b+m.sqrt(d))/(2*a)
    print('Root r1=',r1)
    print('Root r2=',r2)
elif d==0:
    print("Roots are equal")
    r1=-b(2*a)
    r2=r1
    print("Rootsr1",r1)
    print("Rootsr1",r2)
else:
    print("Roots are imaginery")

    
