#create a function print_emp_data()
#if we pass id as argument that function will print emp_name
#if we pass id as property=desig ,it will print emp_name &desig

employe={}
f=open("employee","r")
for lines in f:
    id,name,desig,exp,salary=lines.rstrip("\n").split(",")


    employe[id]={"id":id,"name":name,"exp":exp,"salary":salary}


for k,v in employe.items():
    print(k,v)

def print_emp_data(**kwargs):
    print(kwargs)
    if "id" in kwargs:
        id=kwargs["id"]
        print(employe[id]["name"])

print_emp_data(id="1000") #ajay
# print_emp_data(id=1000,property="desig") #ajay&developer