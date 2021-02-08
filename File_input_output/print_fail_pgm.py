f1=open("names","r")
f2=open("passed","r")
    # name=set()
    # passed=set()
    # for lines in f1:
    #     name.add(lines.rstrip("\n"))
    # for lines in f2:
    #     passed.add(lines.rstrip("\n"))
    #
    # fail=set()
    # fail=name-passed
    # print(fail)


#method 2
#========

def conert_to_set(file):
    file_set=set()
    for lines in file:
        file_set.add(lines.rstrip("\n"))
    return file_set

nameset=conert_to_set(f1)
passset=conert_to_set(f2)
res=nameset-passset
print(res)