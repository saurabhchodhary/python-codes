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
print('Total bill',toatal_bill)