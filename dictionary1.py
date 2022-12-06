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
for x in Student.keys():
    print(x)
for x in Student.values():
    print(x)
for x in Student.items():
    print(x,':',y)
for x in Student:
    print(x,':',student[x])
#partition()
s='I like to eat apples'
t=s.partition('eat')
print(t)
s1='I like to eat apples,apples are my favourite fruit'
t1=s1.rpartition('apples')
print(t1)
l=s.split()
print(l)

s1="apple,banana,gava,kiwi,orange,mango,grapes,lichi"
l1=s1.split(',')
print(l1)

#find()
S='HELLO  WELCOME TO PYTHON CLASS'
l=S.find('WELCOME')
print(l)
#rfind()
j=S.rfind('PYTHON')
print(j)
#strip()
#this can remove the repeated text that we want to remove only
s="  i love my self  "
print(s)
print(s.strip())
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