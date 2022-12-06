"""
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
a=float(input("what is the CGPA 1st ="))
b=float(input("what is the CGPA 2nd ="))
c=float(input("what is the CGPA 3rd ="))
d=float(input("what is the CGPA 4th ="))
if a>b and a>c and a>d:
    print("a has the largest CGPA")
elif b>a and b>c and b>d:
    print("b has the largest CGPA")
elif c>a and c>b and c>d:
    print("c has the largest CGPA")
else:
    print("d has the largest CGPA")
print("this is the end of program ")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
a=float(input("what is the CGPA 1st ="))
b=float(input("what is the CGPA 2nd ="))
c=float(input("what is the CGPA 3rd ="))
d=float(input("what is the CGPA 4th ="))
if a>b and a>c and a>d:
    print("a has the largest CGPA")
elif  b>c and b>d:
    print("b has the largest CGPA")
elif c>d:
    print("c has the largest CGPA")
else:
    print("d has the largest CGPA")
print("this is the end of program ")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#check that the variable is vowel or non vowel
x = str(input("Enter the single character alphabet="))
if x=="a" or x=="A" or x=="E" or x=="e" or x=="i" or x=="I" or x=="o" or x=="O" or x=="U" or x=="u" :
    print (x,"is a vowel ")
else:
    print (x,"is a non- vowel")
print("this is the end of program ")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
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
    print("big2",big)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#write a program wheither the student is allowed to give the final exam based on the attendance table given below
att=float(input("Enter your attendance ="))
if att>=75:
    print("Eligible")
elif att>70 and att<=74:
     ATT=att+5
     print("attendance after bonus",ATT)
     print("Eligible")
else:
    print("not eligible")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
s="abcdabcdabcdefghefh"
c=s.count('a')
print('a is appeared =',c)
S=s.index('abc')
print(S)
#change the case of value
s="A GOOD PROGRAMMER"
print(s.lower())
s="a good programmer"
print(s.upper())
s="a gOOD proGRAMMER"
print(s.title())
print(s.capitalize())
t=('a','b','c','d')
s="#"
m=s.join(t)
print(m)
a="AppleBananaKiwi"
#"istitle" check the case is title or not
print(a.istitle())
#"isalpha" check the alphabets
print(a.isalpha())
#"isalnum" check the alfa numberic value
print(s.isalnum())
#"isnumeric" check the numeric value
c="12212307"
print(c.isnumeric())
#"isspace" check the only space is present
C="    "
print(C.isspace())
print(C.count(' '))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
name=input("Enter teh name:")
reg=int(input("Enter the regi. number:"))
la=int(input("Enter total number of lecture delivered :"))
ld=int(input("Enter total number of lecture attended :"))
atp=(la/ld)*100
atp=input('Enter your attendance')
if atp >= 75:
    print("student is Eligible for ETE")
elif atp>=70 and atp<=74:
    if atp==74:
        new = 75-atp
        print("student is Eligible for ETE")
    elif atp==73:
        new = 75-atp
        print("student is Eligible for ETE")
    elif atp==72:
        new = 75-atp
        print("student is Eligible for ETE")
    elif atp==71:
        new = 75-atp
        print("student is Eligible for ETE")
    else:
        print("student is Eligible for ETE")
else:
    print("student is Not Eligible for ETE")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
a="what is ur name "
b='what is ur name '
print(type(a))
print(type(b))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
t=('a','b','c','d') s="#"
m=s.join(t)
print(m)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
c=int(input())
a=2
b=4
c=5
print(a,b,c,sep="#")

x=1432
d=bin(x)[2:]
print(d)

a=1294744
c=bin(a)
print(c)

c=complex(a)
print(c)

c=float(a)
print(c,)

c=oct(a)
print(a)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# looping statement also known as repitive stat. and herafive statement 

syntax of for loop 
for iterate variable  in sequence:
    body of for loop 


for a in range (5):
    print("ARYAN",end="&")

for i in range (1,21):
    print(i)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=int(input("ENter the value:"))
sum=0
for a in range (1,n+1):
    sum=sum+a
    print('sum=',sum)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=int(input("ENter the value:"))
for a in range (1,n+1):
    print(n)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#even number sum 
n=int(input("Enter the value"))
sum=0
for a in range (1,n+1,2):
            sum=sum+a
            print("sum=",sum)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# odd number sum 
n=int(input("Enter the value"))
sum=0
for a in range (2,n+1,2):
            sum=sum+a
            print("sum=",sum)          
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=int(input("Enter the value"))
fact=1
for a in range (1,n+1):
    fact=fact*a
print("factorial of",n,"is",fact)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=int(input("Enter the value"))
total=0
while n<=10:
    total=total+n
    n=n+1
print('total',total)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#            
reg=int(input("Enter the reg. id="))
total=0
while reg>0:
    r=reg % 10
    total=total+r
    reg=reg//10
    print("sum of reg. id is",total)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
Number = int(input("Please Enter any Number: "))
Reverse = 0
while(Number > 0):
    Reminder = Number %10
    Reverse = (Reverse *10) + Reminder
    Number = Number //10
print("\n Reverse of entered number is = %d" %Reverse)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
l1=[1,2,3]
l2=[1,2,3]
print(l1 is not l2 )#check whether the number is panidrom or not
n=int(input("Enter the number="))
m=n 
rev=0
while n>0:
    rem = n % 10
    rev = rev * 10 + rem 
    n= n//10
if m==rev:
    print(m,'is polaindrome number')
else:
    print(m,'is not a polaindrome number ')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#library is the place in the ide from which we can easy calculate the program there are many elements in python library 
#syntax
import random as r 
#a) random() enters random float value from (0-1)
x=r.random()
print(x)
#b randint() enters random integer b/w the given range 
y=r.randint(1,10)
print(y)
#c randrange() enters the random value with a specific step-size
z=r.randrange (20,30,4)
print(z)
z=r.choice("aryan")
print(z)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#check whether the number is panidrom or not
n=int(input("Enter the number="))
m=n 
rev=0
while n>0:
    rem = n % 10
    rev = rev * 10 + rem 
    n= n//10
if m==rev:
    print(m,'is polaindrome number')
else:
    print(m,'is not a polaindrome number ')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=int(input("Enter the no to check if it is prime="))
dc=0
for a in range (1,n+1):
    if n%a == 0:
        dc=dc+1 
if dc==2 :
    print(n,"is prime ")
else:
    print(n,"not prime")

m=(input("Enter the mobile number:-"))
length=(len(m))
if length==10:
    if m.isdigit()==True:
        print(m,"valid mobile number")
    else:
        print("Enter the digits only")
else :
    print("not vallid number")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
x=1987.67
x=int(x)
x=x%10
print(x)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
s1='Z B C'
s2='X B D'
print(s1<s2)
print(chr(122))

import random as r 
l=[]
for a in range (5):
    x=r.randint(10,11)
    l.append(x)
print('Random number are',l)

for x in range (1,10001):
    dc=0
    for a in range (1,11):
        if x%a==0:
            dc=dc+1
        if dc==10:
            print(x)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#           
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
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# table of n and m
n=int(input("n:"))
m=int(input("m:"))
for x in range (n,m+1):
    for a in range (1,11):
        print(x*a,end='  ')
    print()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#    
a=(input())
c=int(a[0])
d=int(a[-1])
print(c+d)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
import math as m
a=int(input())
#len=len(str(a))
len=m.log10(a)
c=int(len)
last=a % 10
first=a//(10**(c))
total = first + last
print(total)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
l=["apple","bannana","mango"]
print("%s"%(l,sep=("\n")))
print(l)
for x in l:
    print(x)
t=(10,20,30,40,50,60)
print(t)
for x in t :
    print(x)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
x=(input())
c=chr(ord(x)+17)
v=chr(ord(x)+20)
print("%s %s"%(c,v))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=int(input())
t1=int(input())
t2=int(input())
tn=3
while tn <=(n):
    t3=t1+t2
    print(t3)
    t1=t2
    t2=t3
    tn=tn+1
 # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#   
n=int(input())
m=n
total=0
while n>0:
    rem=n%10
    total=total +(rem**3)
    n=n//10
if m ==total:
    print( m,"is armstrong number" )
else:
    print(m, "is not armstrong number")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
m=(input())
a=m[0]
b=m[1]
c=m[2]
#d=m[3]
e=int(a)
i=int(b)
o=int(c)
#d=int(d)
v=(e**3)
f=(i**3)
g=(o**3)
#h=(d**3)
if int(m)==(v+f+g):
    print("True")
else:
    print("False")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
m=(input())
a=m[0]
b=m[1]
c=m[2]
#d=m[3]
e=int(a)
i=int(b)
o=int(c)
#d=int(d)
v=(e**3)
f=(i**3)
g=(o**3)
#h=(d**3)
i=v+f+g
n=int(m)
print(bool(n==i))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
l=[]
n=int(input())
p=0
while n>0:
   r=n%10
   dc=0
   for a in range(1,r+1):
       if r%a==0:
           dc=dc+1
   if dc == 2:
       p=p+1
       l.append(r)
   n=n//10
print('No of prime numbers are:-',p)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=input()
c=n[::-1]
v=(n==c)
print(bool(v))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def funct_name(arguments):
        #body of function
    
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def display():
    print("K22GP")
display()
display()
display()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def display(a=100,b=200,d=400):
    print(a)
    print(b)
    print(d)
display(10,20,30)
print()
display(40,50,60)
print()
display(70,80,90)
print()
display()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def arthmatic(a,b,c):
    print(a+b+c)
    print(a-b-c)
    print(a*b*c)
    print(a//b//c)
    print(a%b%c)
    print(a/b/c)
a=int(input('Enter the first value from set a='))
b=int(input('Enter the first value from set b='))
c=int(input('Enter the first value from set c='))
arthmatic(a,b,c)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def calculate(n):
    total=0
    for x in n:
        total=total+int(x)
    print("Total sum=",total)
number=input('Enter the number=')
calculate(number)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def calculate(n):
    total=0
    for x in n:
        total=total+int(x)
    return total
number=input('Enter the number=')
t=calculate(number)
print('Total sum=',t)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def calculate(n):
    l=len(n)
    total=0
    for x in range(l):
       total=total+int(n[x])
    return total
number=input('enter the number:-')
t= calculate(number)
print('total sum:-',t)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#write a function that calculates the average of 5 subjects
def average(s1,s2,s3,s4,s5):
    for x in range (5,):
        average =((s1+s2+s3+s4+s5)/5)
    return average
s1=input("enter the number of subject1:-")
s2=input("enter the number of subject2:-")
s3=input("enter the number of subject3:-")
s4=input("enter the number of subject4:-")
s5=input("enter the number of subject5:-")
t=average()
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# Write a program for giving output the date and month with the response to the given input number
a=int(input("Enter the day:"))
n=['January','Februrary','March','April','May','June','July','August','September','October','November','December']
d=['Sunday','Tuesday','Wednesday','Thursday','Friday','Saturday']
if a>=1 and a<=31:
    print(a,n[0])
elif a>=32 and a<60:
   print(a-31,n[1])
elif a>=60 and a<91:
    print(a-31-28,n[2])
elif a>=91 and a<121:
    print(a-31-28-31,n[3])
elif a>=121 and a<152:
    print(a-31-28-31-30,n[4])
elif a>=152 and a<182:
    print(a-31-28-31-30-31,n[5])
elif a>=182 and a<213:
    print(a-31-28-31-30-31-30,n[6])
elif a>=212 and a<244:
    print(a-31-28-31-30-31-30-31,n[7])
elif a>=244 and a<274:
    print(a-31-28-31-30-31-30-31-31,n[8])
elif a>=274 and a<305:
    print(a-31-28-31-30-31-30-31-31-30,n[9])
elif a>=305 and a<335:
    print(a-31-28-31-30-31-30-31-31-30-31,n[10])
elif a>=335 and a<=366:
    print(a-31-28-31-30-31-30-31-31-30-31-30,n[11])
else:
    print("invalid")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
# Write a program for checking whether the entered month is a under which season
a=(input("Enter the Month name:"))
a=a.capitalize()
n=['January','Februrary','March','April','May','June','July','August','September','October','November','December']
if  n==[11] or a==n[0] or n==[1]:
    print("Winter Season")
elif n==[2] or a==n[3] or n==[4]:
    print('Spring Season')
elif n==[5] or a==n[6] or n==[7]:
    print('Summer Season')
elif n==[8] or a==n[9] or n==[10]:
    print('Autumn Season')
else:
    print('Enter valid month')

# In a nearby theature one scheme is announced that 1 purchase of the ticket will get a total of 10% of discount of the total cost of the ticket.The scheme will be applicable only if their is a bulk booking of more than 20 tickets. If someone has a special coupon card then the discount will be 2%. The coustmer can also purchase some refreshment an dthe additional cost of 50 ruppes per person. Ticket cost for class A is 150 and class B is 75 .
# Write a program to calculate the total cost as per the given scheme.
# Constraints:- either the class a and classs b min of 5 tickets and maximum 40 is only allowed. if their is a purchase is less then 5 then print the message "ither the class a and classs b min of 5 tickets and maximum 40 is only allowed."

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
n=int(input())
s=0
for i in range (1,n):
    if n%i==0:
        s=s+i
if s==n:
    print(n,'is a perfect number')
    print('Perfect square =',n*n)
else:
    print(n,'is not a perfect number')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def perfect(n):
    s=0
    for a in range (1,n):
        s+=a
    if s==n:
        return 1
    else:
        return -1
x=int(input('Enter the number'))
a=perfect(x)
if a==1:
    print(x,'is perfect number')
else:
    print(x,'is not perfect number')
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
import math as m
def sqrt(n):
    r=m.pow(n,0.5)
    return r
x=int(input('Enter the number'))
print('sqrt of',x,'is=',sqrt(x))
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def digit(n):
    a=1
    while n>o:
        r=n%10
        if a<r:
            a=r
        n=n//10
    print('Largest digit=',a)
digit (78569234)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
def pow(n,p):
    r=1
    for a in range(1,p+1):
        r=r*n
    print('Power=',r)
x=int(input('Enter no.='))
e=int(input('Enter exxponent='))
pow(x,e)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
x=[1,2,3,4,5,6]
del(x[5])
x.append(60)
x.insert(1,7)
A=[50,60,70]
x.extend(A)
print(x)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#

# Python Dictionaries
# DICT={key:value,key:value,key:value...}
student={'name':'paramjeet sangwan','reg':12212477,'section':'K22GP','rollno':32}
print(student)
student['branch']='CSE'
print(student)
student['section']='K22GQ'
print(student)
print(student['reg'])
# Dict.keys()
print(student.keys())
# Dict.values()
print(student.values())
# Dict.get()
print(student.get('section'))
# Dict.update()
print(student.update())
# Dict.pop
print(student.pop('rollno'))
# Dict.popitem
print(student.popitem)
# copy()
Car={'Brand':'March','Model':'Vitara','Year':2022}
Vehicle=Car.copy()
print(Vehicle)
#frontkeys()
Keys=('name1','name2','name3')
Values=100
D=dict.fromkeys(Keys,Values)
print(D)
#Setdefault()
V=Car.setdefault('Brand','Hundai')
print(V)
print(Car)
Student={'name':'ajay','age':20,'course':'btech','reg':12213745,'section':'k22gp','roll no':58}
#for x in 'anydictionary'
#print all keys of dictionary using loop
for x in Student:
    print(x)
for x in Student:
    print(student[x])
for x in Student.Keys():
    print(x)
for x in Student.Valuse():
    print(x)
for x in Student.items():
    print(x,':',y)
for x in Student:
    print(x,':',student[x])
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
d={}
k=[]
v=[]
n=int(input('Enter the no. of dish items:'))
for x in range(n):
    name=input('Enter new dish name=')
    price=int(input('Enter dish price='))
    k.append(name)
    v.append(price)
for x in range(n):
    d.update({k[x]:v[x]})
toatal_bill=0
for x in d.values():
    toatal_bill=toatal_bill+x
print('bill slip')
for x,y in d.items():
    print(x,':',y)
print('Totalbill:-',toatal_bill)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#partition()
s='I like to eat apples'
t=s.partition('eat')
print(t)
s1='I like to eat apples,apples are my favourite fruit'
t1=s1.rpartition('apples')
print(t1)
l=s.split()
print(l)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
s1="apple,banana,gava,kiwi,orange,mango,grapes,lichi"
l1=s1.split(',')
print(l1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#find()
S='HELLO  WELCOME TO PYTHON CLASS'
l=S.find('WELCOME')
print(l)
#rfind()
j=S.rfind('PYTHON')
print(j)
#trip()
s="  i love my self  "
print(s.strip())

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#splitlines()
s='I love myself\nonly'
l=s.splitlines()
l1=s.splitlines(True)
print(l,l1,sep='\n')
#replace()
s="I like apples,apples are my favourite fruit"
s1=s.replace('apples','mango')
print(s1)
#join()
#join method takes all the items in an iteleration and join them into one string.
# string must be specified as a seprator
s=['INDIA','CHINA','RUSSIA','FRANCE']
s1=' # '.join(s)
print(s1)
D={'K1':'V1','K2':'V2','K3':'V3'}
a1=" # ".join(D)
print(a1)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
person1={'name':'abc','age':20}
person2={'name':'xyz','age':30}
person3={'name':'pqr','age':40}
family={'p1':person1,'p2':person2,'p3':person3}
print(family)
print(person2[0])
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#new_d={key:value for loop(key,value) in iterable}
l=['apple','onion','burger','sweetcorn']
m=['fruit','vegetable','snack','soup']
z=zip(l,m)
menu={k:v for(k,v)in z}
print(menu)
d={x:x**2 for x in range (1,5)}
print(d)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#
#fromkeys()
dict={}
dic=dict.fromkeys(range (1,6),'abc')
print(dic)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>#"""
