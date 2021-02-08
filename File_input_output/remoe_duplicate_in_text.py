f=open("text","r")
lst=[]
for lines in f:
    lst.append(lines.rstrip("\n"))
print(set(lst))


# st=set()
# for lines in f:
#     st.add(lines.rstrip("\n"))
# print(st)