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

"""logic
a) extract last value form input and save in the variable 
b) next extracted value should not replace previous extracted value 
c) after extracting reduce the original input to 1 digit less
d) repeat steps abc the input is greater than 0
