# Check the mobile number is valid or not 

m=(input("Enter the mobile number:-"))
length=(len(m))
if length==10:
    if m.isdigit()==True:
        print(m,"valid mobile number")
    else:
        print("Enter the digits only")
else :
    print("not valid number")


