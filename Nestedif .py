#nested if statement refers to the condition in which we can use if with in the first if statement 
"""
if con :
    block for if :
       if con:
        block for if: 
else:
    block of else
    if con:
        block for if 
end of program 
"""
gender=input("Enter the sex of voter as B or G :")
age=int(input("Enter the age of voter "))
if age >=18:
    if gender == "b" or gender == "B":
        print("Allowed in room no. 20")
        else :
            print("Allowed for vote in room no. 25")
else: 
    print("Not allowe dto vote ")