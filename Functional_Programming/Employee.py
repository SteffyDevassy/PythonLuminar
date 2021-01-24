employee=["ajay","vijay","anil","danie","tom","joy"]

#convert all emp names to uppercase
upp=list(map(lambda name:name.upper(),employee))
print(upp)

#print all emp name starting with a
start=list(filter(lambda name:name[0]=="a",employee))
print(start)


