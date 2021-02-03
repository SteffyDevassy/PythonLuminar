
lst=[9,8,7,6,4,3,2]
#10,9,8,7,3,2,1

lst1=[10,11,8,4,3]  #11,12,9,3,2
#no>5 no+1  else no-1
pat=[]
for i in lst:
    if(i>5):
        pat.append(i+1)
    else:
        pat.append(i-1)
print(lst)
print(pat)

#remove an element from list
lst.pop(5)
lst.remove(9)
print(lst)

#updation
lst[0]=22
print(lst)

