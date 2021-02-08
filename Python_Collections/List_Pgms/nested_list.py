students=[
    [100,"arun","bca",145],
    [101,"arjun","mca",125],
    [102,"varun","bcom",155],
    [103,"tarun","bca",130],
    [104,"jarun","mca",140]
]

#print student names

for st in students:
    print(st[1])


#print total of all students
total=0
for st in students:
    total+=st[3]
print("total=",total)

#list the details of student whose course=mca

for st in students:
    if(st[2]=="mca"):
        print(st)

#mca?bcom?bca?

m=0
b=0
bc=0
for st in students:
    if(st[2])=="mca":
        m+=1
    elif(st[2]=="bca"):
        b+=1
    elif(st[2]=="bcom"):
        bc+=1
print("mca=",m)
print("bca=",b)
print("bcom=",bc)

#hightest total

print("MAx total")
# for student in students:
# m=[max(student) for student in students]
# print(m)
m=max(students,key=lambda x: x[3])
print(m[3])