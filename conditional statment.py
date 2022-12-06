# conditional statement  if (true consider only) , if - else (consider both true and false outcomes ) , if - elif - else () 
# syntax for if conditional statement 
"""if condition:
    body of if statement1 [if block]
    statement2
    statement3
print()"""

a=int(input("Enter the values="))
if a>0:
    S=a*a
    print ("square=",S)
print("End of program")

#syntax of if - else conditional statement
"""if condition:
    block of if 
else:
    block of else 
    """
a=int(input("Enter the value="))
if a> 0:
    s=a*a
    print ("square=",s)
else:
    c=a**3
    print ("cube=",c)
print ("End of program")

# check the largest nummber 
a=int(input("Enter the first value="))
b=int(input("Enter the second value"))
if a>b:
    print(a," value is greater " ,b)
else b>a:
    print(b,"value is greater",a)
print ("End of program")
    
# if -elif -else conditional statement
#this is only used for multiple conditional statement.
#syntax of if elif else statement 
"""
if cond :
    block of if 
elif cond :
    block of elif 
# we can use elif as per our need 
else :
    block of else 
"""
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
    
