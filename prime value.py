# by the help of for statement check whether the vallue is prime or not

n=int(input("Enter the no to check if it is prime="))
dc=0
for a in range (1,n+1):
    if a%a==0:
        dc=dc+1 
if dc==2 :
    print(n,"is prime ")
else:
    print(n,"not prime")

# unitl the ited value belongs to the sequence then the statement repeats itself 
L=[]
n=int(input("n:"))
m=int(input("m:"))
print("all the prime number between n to m are ")
for x in range (n,m):
    dc=0
    for a in range (1,x+1):
        if x % a==0:
            dc=dc+1
    if dc==2:
        print(x)
        L.append(x) 
print('total prime numbers are=',len (L))

# table of n and m

n=int(input("n:"))
m=int(input("m:"))
for x in range (n,m+1):
    for a in range (1,11):
        print(x*a,end='  ')
    print()




 

