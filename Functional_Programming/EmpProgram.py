from functools import *
class Employee:
    def __init__(self,eid,ename,exp,sal,desig):
        self.eid=eid
        self.ename=ename
        self.exp=exp
        self.sal=sal
        self.desig=desig
    def __str__(self):
        return self.ename

#read from file
f=open("employe","r")
employees=[]
for lines in f:
    eid,ename,exp,sal,desig=lines.rstrip("\n").split(",")
    employees.append(Employee(eid,ename,desig,sal,exp))

#highest salary
highsal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
               list(map(lambda emp:emp.sal,employees)))
print(highsal)
print("\n")

#print highest salaries emp details
employ=list(filter(lambda emp:emp.sal==highsal,employees))
for emp in employ:
    print(emp.ename)

#find highest salary whose desig=developer
developer=list(filter(lambda emp:emp.desig=="developer",employees))
devsalary=list(map(lambda emp:emp.sal,developer))
employ=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,devsalary)

print(employ)

#find highest salary whose desig=developer in single line

deve_high_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                    list(map(lambda emp:emp.sal,list(filter(lambda emp:emp.desig=="developer",employees)))))
print(deve_high_sal)