#values stored in key-value pairs

student={"rollno":100,"name":"ajay","course":"mca"}
#access values using keys
print(student["rollno"])

#duplicate keys are not allowed,but duplicate values are allowed



#updation
student["name"]="vijay"
print(student)

#adding new ele
student["gender"]="male"
print(student)