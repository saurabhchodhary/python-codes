"""
A set is a mutable data type that contains an unordered collection of items.

Every element in the set should be unique (no duplicates) and must be immutable (which cannot be changed). But the set itself is mutable. We can add or remove items / elements from it. 

The main uses of sets are:
 Membership testing
Removing duplicates from a sequence
Performing mathematical operations such as intersection, union, difference, and symmetric difference
A set is represented with { }.

Creation of sets
A set is created by placing all the items (elements) inside curly braces {}, separated by comma or by using the built-in function set().


"""
myset = set()
print(myset) 
# will print empty set.
print(type(myset)) 
# will print type of myset.

"""
Note : Empty curly braces { } does not make an empty set in Python, it makes an empty dictionary instead. Dictionary data type is introduced in the upcoming lessons.
"""

test = { } 
print(type(test))
