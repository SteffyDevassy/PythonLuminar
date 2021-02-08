employee=[
    [1001,"ajay","qa",1981,2003],
    [1002,"vijay","developer",1992,2008],
    [1003,"arun","ba",1989,2010],
    [1004,"amal","developer",2009,2014],
    [1004,"vimal","developer",1987,1989],
]

#print all emp designation
print("\"all emp designation\"")
for emp in employee:
    print(emp[2])
print("\n")

#print all emp whose design=developer
print("emp whose design=developer")
for emp in employee:
    if(emp[2]=="developer"):
        print(emp[1])
print("\n")

#print all emp those who are working in 1980's
print("emp those who are working in 1980's")
for emp in employee:
    if(emp[3] in range(1980,1990) or emp[4]in range(1980,1990)):
        print(emp[1])
print("\n")



#print all emp details whose experience >9years
print("emp whose experience >9years")
for emp in employee:
    diff=emp[4]-emp[3]
    if(diff>9):
        print(emp)
print("\n")