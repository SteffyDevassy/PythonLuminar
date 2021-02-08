#step 1
#create file refernce
#f=open("path","mode of operation")


#file->copy path-> paste path

f=open("text","r")
# print(f)  # a refernce is printed
lst=[]
for lines in f:
    lst.append(lines)
print(lines)
print(lst)


data="hello\n"
data=data.rstrip("\n")
print(data)

data="\nhello"
data=data.lstrip("\n")
print(data)