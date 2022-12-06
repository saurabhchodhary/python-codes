#write a program wheither the student is allowed to give the final exam based on the attendance table given below 

att=float(input("Enter your attendance ="))
if att>=75:
    print("Eligible")
elif att>70 and att<=74:
     ATT=att+5
     print("attendance after bonus",ATT)
     print("Eligible")
else:
    print("not eligible")
