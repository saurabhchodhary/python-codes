# looping statement also known as repitive stat. and herafive statement 
"""syntax of for loop 
for iterate variable  in sequence:
    body of for loop 
"""
for a in range (5):
    print("ARYAN",end="&")

for i in range (1,21):
    print(i)

n=int(input("ENter the value:"))
sum=0
for a in range (1,n+1):
    sum=sum+a
    print('sum=',sum)

n=int(input("ENter the value:"))
for a in range (1,n+1):
    print(n)

#even number sum 
n=int(input("Enter the value"))
sum=0
for a in range (1,n+1,2):
            sum=sum+a
            print("sum=",sum)

# odd number sum 
n=int(input("Enter the value"))
sum=0
for a in range (2,n+1,2):
            sum=sum+a
            print("sum=",sum)
            
n=int(input("Enter the value"))
total=0
while n>=10:
    total=total+n
    n=n+1
print('total',total)

reg=int(input("Enter the reg. id="))
total=0
while reg>0:
    r=reg % 10
    total+rangereg=reg//10
    print("sum of reg. id is",total)
# is operator is used for checking that the given variable are equal or not 

X="Helllo"
Y="hello "
Z= X is Y
print (Z)

x=15
y=15
z=x is y
print(z)

l1=[1,2,3]
l2=[1,2,3]
print(l1 is l2 )
print (id(l1))
print(id(l2))
