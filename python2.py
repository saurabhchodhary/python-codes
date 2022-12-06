# Write the program in python to find the total sum of list and minimum and maximum.
"""
import functools as ft
l=[57,43,69,38,72,56,29,68,83]
s=ft.reduce(lambda a,b : a+b,l)
print('total sum=',s)

mx=ft.reduce(lambda a,b : a if a>b else b,l)
mn=ft.reduce(lambda a,b:a if a<b else b,l)
print('Maximum=',mx)
print('Minimum=',mn)
"""

# Write a program in python that filter the list of n number elements to the new list of prime number only.
"""
l=[]
n=int(input('Enter the size of list='))
for x in range(n):
    e=int(input('Enter new list element='))
    l.append(e)
def func(x):
    dc=0
    for a in range(1,x+1):
        if x%a==0:
            dc+=1
    if dc == 2 or dc==1:
        return True
    else:
        return False
nl=filter(func,l)
print('Prime number list are')
print(list(nl))
"""

# Calculate the sum of series of 1^a+2^a+3^a+.............+n^a.
"""
import functools as ft
l=[]
n=int(input('Enter the size of list='))
c=int(input('Enter the exponent='))
for x in range (1,n+1):
    l.append(x**c)
s=ft.reduce(lambda a,b:a+b,l)
print('total sum=',s)
"""

"""
l=[]
n=int(input('Enter the size of list='))
for x in range (n):
    e=float(input('Enter new lsit element='))
    l.append(e)
area=map(lambda r : 3.14 *(r**2),l)
print('Area of different circles are')
for a in area:
    print(a)
"""

# Object-Oriented Programming (An object is a collection of data and methods ). Object is also known as instance of Class. Class is a Blue print of program.
"""Syntax for crearing class
   class abc:
        a=10
    o=abc()
    print(o.a)
    """
"""   
class abc:
    a=39
o=abc()
print(o.a)
"""

"""
class student:
    def __init__(self,nm,b,r,sec):
        self.name=nm
        self.branch=b
        self.reg=r
        self.section=sec
    def display(self):
        print('student name=',self.name)
        print('student reg=',self.reg)
        print('student branch=',self.branch)
a=student('Aryan','CSE',12213745,'K22GP')
a.display()
b=student('xyz','abc',12345677,'K22SH')
b.display()
c=student('sfd','ert',12324352,'K22HS')
c.display()
"""

# Create a class  with cyliner in python having one init method use to initialize class variable radius and height , the class further contain 2 user defined function name calculate and display, calculate function is used to calculate area and volume of cylinder and display is used to display the calculated elements.

"""
class cylinder:
    def __init__(self,R,H):
        self.radius=R
        self.height=H
        self.volume=3.14*(self.radius**2)*self.height
        self.area=2*3.14*self.radius*self.height
    def display(self):
        print('Volume of cylinder',self.volume)
        print('Area of cylinder',self.area)
r=float(input('Enter radius:-'))
h=float(input('Enter height:-'))
c1=cylinder(r,h)
c1.display()
r2=float(input('Enter radius:-'))
h2=float(input('Enter height:-'))
c2=cylinder(r2,h2)
c2.display()
r3=float(input('Enter radius:-'))
h3=float(input('Enter height:-'))
c3=cylinder(r3,h3)
c3.display()
"""
"""
scout=0
class student:
    def __init__(self,nm):
        self.name=nm
        student.scout= scout+1
    def display(self):
        print('Name:-',self.name)
a=student('abc')
b=student('pqr')
c=student('xyz')
a.display()
b.display()
c.display()
print('Total student are=',student.scout)
"""

# Properties of class :-
# 1. Encapsulation             2. Abstraction                   3. Inheritance               4. Polymorphism
# How to create the empty class
"""
class student:
    pass
"""
# Overloading is a kind of Polymorpism which means class having many '__init__' function.
# '__init__' is a special type of class methoid which get automatically executed when a new class is given and also known as Constructor of class, and we can call init funcgtion to every time an object is created from a class.
# Single Inheritence
"""
class student:
    def __init__(self,c1,c2,c3,c4,c5,m1,m2,m3,m4,m5):
        self.course1=c1
        self.course2=c2
        self.course3=c3
        self.course4=c4
        self.course5=c5
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
        self.marks4=m4
        self.marks5=m5
        self.per=((self.marks1+self.marks2+self.marks3+self.marks4+self.marks5)/500)*100
    def display(self):
        print('course name=',self.course1)
        print('course name=',self.course2)
        print('course name=',self.course3)
        print('course name=',self.course4)
        print('course name=',self.course5)
        print('course marks=',self.marks1)
        print('course marks=',self.marks2)
        print('course marks=',self.marks3)
        print('course marks=',self.marks4)
        print('course marks=',self.marks5)
        print('percentage=',self.per)
a=student('python','html','math','physics','mec',100,100,100,100,75)
a.display()
"""

"""
class area:
    def __init__(self,s):
        self.side=s
        self.ase=self.side**2
        print('Area of square=',self.ase)
    def __init__(self,l,b):
        self.length=l
        self.breath=b
        self.ar=self.length*self.breath
        print('Area of rectange=',self.ar)
    def __init__(self,l,b,h):
        self.length=l
        self.breath=b
        self.height=h
        self.vc=self.length*self.breath*self.height
        print('Volume of cuboid',self.vc)
a=area(10)
b=area(10,20)
c=area(10,20,30)
"""

#Find the area of square and rectangle?
"""
class calculate:
    def __init__(self,*args):
        if len(args)==1:
            self.side=args[0]
            print("Area of square=",self.side*self.side)
        if len(args)==2:
            self.length=args[0]
            self.breadth=args[1]
            print("Area of rectange=",self.length*self.breadth)
a=calculate(int(input("Enter side:-")))
b=calculate((int(input("Enter length:-"))),(int(input("Enter Breath:-"))))
"""

# Display the details of person.
"""
class person:
    def __init__(self,nm,a):
        self.name=nm
        self.age=a
    def display1(self):
        print("Name=",self.name)
        print("Age=",self.age)
class student(person):
    def __init__(self,nm,a,r,b,s):
        person. __init__(self,nm,a)
        self.reg=r
        self.branch=b
        self.section=s
    def display2(self):
        person.display1(self)
        print("Reg=",self.reg)
        print("branch=",self.branch)
        print("section=",self.section)
a=student(input("Enter Name:-"),int(input("Age:-")),int(input("Enter reg.:-")),input("Enter branch:-"),input("Enter section:-"))
a.display2()
"""
"""
class employee:
    def __init__(self,nm,age,add):
        self.name=nm
        self.age=age
        self.address=add
    def display1(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Address=",self.address)
class department(employee):
    def __init__(self,nm,age,add,com,dept,role):
        employee. __init__(self,nm,age,add)
        self.company=com
        self.deparment=dept
        self.role=role
    def display2(self):
        employee.display1(self)
        print("Company=",self.company)
        print("Department=",self.deparment)
        print("Role=",self.role)
a=department(input("Enter Name:-"),int(input("Age:-")),(input("Enter Address:-")),input("Enter Company:-"),input("Enter Department:-"),input("Enter Role:-"))
a.display2()
"""

# Multi Inheritence 
"""
class person:
    def __init__(self,nm,a):
        self.name=nm
        self.age=a
class employee(person):
    def __init__(self,nm,a,c,d,s):
        person. __init__(self,nm,a)
        self.company=c
        self.dept=d
        self.sal=s
class bonus(employee):
    def __init__(self,nm,a,c,d,s):
        employee. __init__(self,nm,a,c,d,s)
        if self.sal >=10000:
            self.bonus=1000
        else:
            self.bonus=500
    def display(self):
        print("Name",self.name)
        print("age",self.age)
        print("Company",self.company)
        print("Salary",self.sal)
        print("Bonus",self.bonus)
        print("Total salary",self.sal+self.bonus)
a=bonus(input("Enter Name:-"),int(input("Age:-")),input("Enter Company:-"),input("Enter Department:-"),int(input("Enter Salary-")))
a.display()
b=bonus(input("Enter Name:-"),int(input("Age:-")),input("Enter Company:-"),input("Enter Department:-"),int(input("Enter Salary-")))
b.display()
"""

# Sum of 3 numbers. 
"""
class a:
    def __init__(self,f):
        self.first=f
class b(a):
    def __init__(self,f,s):
        a. __init__(self,f)
        self.second=s
class c(b):
    def __init__(self,f,s,t):
        b. __init__(self,f,s)
        self.third=t
        self.sum=(self.first+self.second+self.third)
        self.multi=(self.first*self.second*self.third)
    def display(self):
        print('Sum=',self.sum)
        print('Multiplication=',self.multi)
    def display2(self):
        print('Multiplication=',self.multi)
a=c(int(input("Enter first value:-")),int(input("Enter second value:-")),int(input("Enter third value:-")))
a.display()
"""

"""
class radius:
    def __init__(self,r):
        self.rad=r
class height:
    def __init__(self,h):
        self.height=h
class Volume(radius,height):
    def __init__(self,r,h):
        radius. __init__(self,r)
        height. __init__(self,h)
        self.vol=3.14*self.rad*self.rad*self.height
    def display(self):
        print("volume of cylinder",self.vol)
a=Volume(float(input("Radius="),float(input("height="))))
a.display()
"""
"""
n=list(map(int,input().split(',')))
m=list(map(int,input().split(',')))
a=[]
for i in m:
    if i in n:
        a.append(i)
    else:
        break
print(a)

l=[]
n=int(input())
for x in range(0,n):
    e=int(input())
    l.append(e)
l.sort()
print(l)
l.reverse()
print(l)

"""
"""
n=list(map(int,input().split(' ')))
print(n)
m=int(input())
c=(n[m])
print(len(str(c)))
"""

"""
class Demo:
    _a=10
    def display(self):
        print("value of a=",self._a)
obj=Demo()
obj.display()
print("New value=",obj._a)
class student:
    def getdetails(self,nm,r,b):
        self.name=nm
        self.reg=r
        self.branch=b
class course:
    def getcourse(self,c1,c2,c3,c4,c5):
        self.cn1=c1
        self.cn2=c2
        self.cn3=c3
        self.cn4=c4
        self.cn5=c5
class marks:
    def getmarks(self,m1,m2,m3,m4,m5):
        self.cm1=m1
        self.cm2=m2
        self.cm3=m3
        self.cm4=m4
        self.cm5=m5
        self.total=(self.cm1+self.cm2+self.cm3+self.cm4+self.cm5)
class result(student,course,marks):
    def displayresult(self):
        self.per=(self.total/500)*100
        self.cgpa=self.per//10
        print("Name=",self.name)
        print("Reg=",self.reg)
        print("Branch=",self.branch)
        print("course Name=",self.cn1,"Marks=",self.cm1)
        print("cgpa=",self.cgpa)
a=result()
# a.getdetails("abc",10,"CSE")
# a.getcourse("PY","PHY","MECH","MATH","CHEM")
# a.getmarks(100,99,100,98,95)
# a.displayresult()
NAME=input("Enter name of student=")
REG=int(input('Enter reg='))
B=input("Enter branch=")
CN1=input("Enter course name=")
CM1=int(input("Enter course marks="))
CN2=input("Enter new course name= ")
CM2=int(input("Enter new course marks="))
a.displayresult()

class student:
    def __init__(self,nm,r,b):
        self.name=nm
        self.reg=r
        self.branch=b
class course:
    def __init__(self,c1,c2,c3,c4,c5):
        self.cn1=c1
        self.cn2=c2
        self.cn3=c3
        self.cn4=c4
        self.cn5=c5
        
        """

"""
class data:
    def getdata(self,r=0,h=0,l=0,b=0):
        self.radius=r
        self.height=h
        self.length=l
        self.breadth=b
class volume1(data):
    def display(self):
        self.vol=3.14*(self.radius**2)*self.height
        print("volume of cylinder=",self.vol)
class volume2(data):
    def dispcone(self):
        self.vol=0.33*3.14*(self.radius**2)*self.height
        print("volume of cone=",self.vol)
class volume3(data):
    def dispcuboid(self):
        self.vol=int(self.length*self.breadth*self.height)
        print("volume of cuboid=",self.vol)
c=volume3()
c.getdata(h=9,l=100,b=20)
c.dispcuboid()
a=volume1()
a.getdata(3.5,5.9)
a.display()
b=volume2()
b.getdata(4.8,7.2)
b.dispcone()
m=[]
s=int(input())#total subhits
for x in range(s):
    l=[]
    n=int(input())#no of elements
    for a in range(n):
        e=int(input())
        l.append(e)
    m.extend(l)

"""
"""
To create an iterator :-

1. __iter()__   :- run iterator object
2. __next()__

in order to avoid the infinite iteration raise the "Stopiteration()" 
"""
"""  
#                                      ITERATION FUNCTION (MAKING OWN DATA TYPE)
class demo:
    def __init__(self,m,x):
        self.i=m
        self.n=x
    def __iter__(self):
        return self 
    def __next__(self):
        if self.i < self.n:
            i=self.i
            self.i+=1
            return i
        else:
            raise StopIteration()

n=demo(int(input()),int(input()))
print(list(n))
for i in n:
    print(i,end=",")
print(type(n))
"""
# ITERATORS ALLOW US TO CREATE OUR WORK WITH LAZY ITERATOR WHICH MEANS THAT YOU CAN USE ITERATION FOR LAZY ,THIS ALLOW YOU TO GET THE NEXT ELEMENT WITHOUT RECALCULATING.
# Generator functions acts like a regular function with one difference that this function uses yield statement. It returnss an iterator.

"""
def test_seq():
    n=int(input())
    m=int(input())
    while n<m:
        yield n
        n=n+1
for i in test_seq():
    print(i,end=' ')
"""

# Reverse string
"""
def reverse_string(s):
    l=len(s)
    for x in range (l-1,-1,-1):
        yield s[x]
for c in reverse_string(str(input())):
    print(c,end='')
"""
"""
#seek command
f=open("abcxyz.txt",'w')
f.write("abcdefghijklmnopqrstuvwvxyz")
f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
f.close()
f=open("abcxyz.txt","r")
f.seek(7)
print(f.read())
f.close()

# tell command 
f=open("abcdxyz.txt",'w')
f.write("abcdefghijklmnopqrstuvwvxyz")
f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
f.close()
m=open("abcdxyz.txt",'r')
print("Current position of file pointer")
print(m.tell())
m.seek(9)
print("New file position is \n")
print(m.tell())
"""
# An error in python can be of 2 types errors are the problems  occurs due to some incorrect syntax which will further stop the execution of code on the other hand exception occur when some internal event occurs which chages the normal flow of problem. Exception are raised when the program is synataxically correct but still the code execution in an error.

#----------------------DIFFERENT WAYS TO HANDLE THE EXCEPTION-----------------------------------------
#1. Try and except :- "Try" block will include the statement which raise the exception and except will catch the error.
"""
l=[1,2,3,4,5]
# print(l[6])
try:
    print("First element=",l[0])
    print("Another element=",l[6])
except:
    print("Not possible")
"""
# Catching specific type of exception

# A Try statement can have more than one except block which is used to handle specific exception or different exception. At a time only one handler is executed on a same time.
"""
try :
    statements
except:
    statements
except:
    statements
"""
"""
def display(n):
    if n<4:
        p=n/(n-3)
    print("value of p=",p)
try:
    #display(3)
    display(5)
#except ZeroDivisionError:                             ----------------ONLY ONE HANDLER IS USED AT A TIME-------------------
#   print("Not possible with denomenator = 0 ")
except NameError:
    print("P not defined")
"""

"""
def display(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("Cannot Divide by Zero")
    else:
        print(c)
display(int(input()),int(input()))
"""
"""
list1=["key1","key2","key3"]
list2=["value1","value2","value3"]
mydict=zip(list1,list2)
print(mydict)
"""

"""
import sys
l=['a',0,2]
for x in l:
    try:
        print("the new entry is=",x)
        r=1/int(x)
        break
    except:
        print("sorry",sys.exc_info()[0],'occured')
        print("Next value")
        print()
print('value of',x,'is=',r)
"""

# Name of the exce. print using exc info() function available inside python module sys. that causes the value error and zero division error.

# What is the difference b/w assertion and exception?
# Assertion in any programming language that helps in to smooth flow of a language code assertions are mainly a kind of assumption that a programmer knows and always wants to be true and puts steps in the code.. so that failuere of the code does not allows the to ececute further.
# Assertion is defined in python with keywork "(assert)"
# Assertion is the boolean exp. that check if the statement is true or false. if the statementis true assertion does nothing but if the statement is false then assertion stops execution oif the program and through then error.
"""
a,b=int(input("Enter a=")),int(input("Enter b="))
# Uses assert to check if b=0
print('The value of a/b is=')
assert b!=0,"Zero not allowed"
print(a/b)
"""
#apllication of assertion =>in testing and quality checking 

#write a program in python that contain some list of batches. The batch will contain a lsit of foodtemperature only hot food is allowed the case is when foodtemp > room temperature.
"""
b=[40,26,29,21,23,30,40]
h= 26
print(" there is a list of all hot temp")
f=[]
for x in b:
    assert x>=26,"batch not allowed"
    f.append(str(x))
    print(f,end="\n")
"""
"""
try:
    a=int(input("Enter a positive integer:"))
    if a <=0:
        raise ValueError("This is not a positive number")
except ValueError as e:
    print(e,"is not a valid integer")
"""    
