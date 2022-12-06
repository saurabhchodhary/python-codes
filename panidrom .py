#check whether the number is panidrom or not
n=int(input("Enter the number="))
m=n 
rev=0
while n>0:
    rem = n % 10
    rev = rev * 10 + rem 
    n= n//10
if m==rev:
    print(m,'is polaindrome number')
else:
    print(m,'is not a polaindrome number ')




