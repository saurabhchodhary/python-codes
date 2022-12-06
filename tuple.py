"""
A tuple is a data type similar to list.
The major differences between the two are: Lists are enclosed in square brackets [] and their elements and size can be changed (mutable), while tuples are enclosed in parentheses () and their elements cannot be changed (immutable). Tuples can be thought of as read-only lists.
Note: Since a tuple is immutable, iterating through tuple is faster than with list. This gives a slight performance improvement.

"""
tuple1=tuple('Aryan')
print(type(tuple1))

mytuple = (1, 2, 3, "Data types") 
# mytuple = 1, 2, 3, "Data types" will also work.
print(type(mytuple))

mytuple = (1,)
# Will print tuple (1,) 
print(type(mytuple))

"""
Multiple-element tuple looks like :
(1, 2, 3) or 1, 2, 3
or
(1, 2, 3,) or 1, 2, 3,
Note : The trailing comma is completely optional for the multiple-element tuples.
Select all the correct statements given below.
"""

n=int(input())
li=[]
for i in range (n):
    a=list(map(int,input()))