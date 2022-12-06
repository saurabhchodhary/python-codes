"""
Dictionary is an unordered collection of key and value pairs.
Note : While other compound data types (like lists, tuples and sets) have only value as an element, a dictionary has a key : value pair
General usage of dictionaries is to store key-value pairs like :
 Employees and their wages
Countries and their capitals
Commodities and their prices
In a dictionary, the keys should be unique, but the values can change. For example, the price of a commodity may change over time, but its name will not change.
Immutable data types like number, string, tuple etc. are used for the key and any data type is used for the value.
Dictionaries are optimized to retrieve values when the keys are known.
Dictionaries are represented using key-value pairs separated by commas inside curly braces {}. The key-value pairs are represented as key : value. For example, daily temperatures in major cities are mapped into a dictionary as { "Hyderabad" : 27 , "Chennai" : 32 , "Mumbai" : 40 }.
Creating a dictionary:

A dictionary can be created in two ways.
 Using the built-in dict() function.
 Assigning elements directly.
1. Using built-in dict() function.
"""
mydict = dict() 
# Creating an empty dictionary called mydict
print(type(mydict)) 
# Printing data type of mydict.
print(mydict)

mydict = dict(Hyderabad = 20, Delhi = 30) 
# A dictionary with two key pairs is created.
print(mydict)

"""
2. Assigning elements directly.

A dictionary is created using direct assignment as follows :

"""
mydict = {1:"one", 2 :"two", 3:"three"}  
# Create a dictionary with three key-value pairs.
print(mydict) 
# Printing the dictionary
print(type(mydict)) 