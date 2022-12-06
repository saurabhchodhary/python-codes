"""
//strings => collections of characters and strings enclosed "" or ''
//syntax is below 
full_name="Aryan Choudhary"
// len function is used for checking the length of the characters
len(full_name)
//string concatination or string combining 
first_name ="Aryan"
last_name="Choudhary"
// add a blank string in b/w name so that there is a space b/w first name and last name 
full_name = (first_name+ " " +last_name)
print(full_name)

//read the character of given range 
X ="Choudhary Aryan Aichra"
//syntax string(index)
print(X[20])
//string slicing 
//string [start index : stop index : step size]"""
print(X[20::4])
x="lovely professional university"
print (x[-1:-5:-1])
# string repetation (*)
print (x*3)

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

