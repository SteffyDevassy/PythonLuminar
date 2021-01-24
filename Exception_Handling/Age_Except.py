#age<18
age=int(input("Enter Age"))
if age<18:
    raise Exception("Sorry, Invalid Age")

#------------------------------
num=input("Enter value")
if type(num)!="int":
    raise Exception("Not integer")