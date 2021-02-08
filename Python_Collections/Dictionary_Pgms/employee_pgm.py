employee={"eid":1000,"desig":"developer","exp":1,"company":"Luminar"}

print(employee["company"])

#check salary included
print("salary" in employee)

#add new ele salary:30000
employee["salary"]=30000
print(employee)

#add 5000 more to current salary
employee["salary"]+=5000
print(employee)

#print key-value pairs
#method1
for emp in employee:
    print(emp,",",employee[emp])

#method2
for k,v in employee.items():
    print(k,v)