"""
List is a data type of Python used to store multiple values of different types of data at a time. List are represented with []. A list can be created by putting comma separated values between square brackets [].
Values stored in the list are accessed using an index.
Python allows negative indexing for lists. The index of -1 refers to the last value of the list, -2 refers to the second last value of the list and so on. 

"""
list1 = [1, 2, "one", "hi"]
print(list1)

"""
A value at a particular index in a list is accessed using
"""
list2 = [4, 5, "hello"]
print(list2[1])

"""
Slicing is used to access a subset of of a list. For a list l = [1, 4, 5, 7, 4, 15], a subset of list from 2nd index to 4th index is obtained by l[2:4] which is equal to [5,7].
"""
list2 = [4, 5, "hello"]
print(list2[1:-1])

"""
In Python, the plus (+) operator is a list concatenation operator and the asterisk (*) operator is the repetition operator. 
"""
list1 = [1, 2, 'one', 'hi']
list2 = [4, 5, 'hello']
print(list1 + list2)
"""
We can print a list multiple times using (*) operator as shown below.  
"""
list2 = [4, 5, 'hello']
print(2 * list2)