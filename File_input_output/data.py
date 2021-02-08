f=open("data","r")
lst=[]
for lines in f:
    words=lines.split(" ")
    for word in words:
        lst.append(word.rstrip(".\n"))
print(lst)