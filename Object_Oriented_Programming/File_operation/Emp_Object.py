from functools import *
class employee:
    def __init__(self,id,name,exp,salary,desig):
        self.id=id
        self.name=name
        self.exp=exp
        self.salary=salary
        self.desig=desig
    def __str__(self):
        return self.name+" "+self.desig+" "+self.salary

f=open("employee","r")
lst=[]


for lines in f:
    id,name,exp,salary,desig=lines.rstrip("\n").split(",")


    ob=employee(id,name,exp,salary,desig)
    lst.append(ob)





for emp in lst:
    print(emp)

print("\n")
# 1. print all emp name in upper case

up=list(map(lambda emp:emp.name.upper(),lst))
print(up)
print("\n")
#----------------------------------------------


#2. print emp details whose designation ="developer"

dev=list(filter(lambda emp:emp.desig=="developer",lst))
for emp in dev:
    print(emp)
print("\n")

#---------------------------------------------
#3 print emp details whose salary >23000

sal=list(filter(lambda emp:int(emp.salary)>23000,lst))
for emp in sal:
    print(emp)

# max=reduce(lambda emp:int(emp.salary))