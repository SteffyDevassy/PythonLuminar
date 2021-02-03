#add a limit of numbers

limit=int(input("Enter limit"))
lst=[]
odd=[]
even=[]
for i in range(1,limit+1):
    lst.append(i)
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(lst)
print(odd)
print(even)
    #store odd and even numbers in to separate list