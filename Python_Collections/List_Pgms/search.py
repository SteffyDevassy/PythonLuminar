lst=[1,2,3,4,5,6,7,8]
n=int(input("Enter no"))

#method 1
flag=0
for num in lst:
    if(n==num):
        flag=1
        break
    else:
        flag=0
if(flag==1):
    print("element found")
else:
    print("element not found")


#method 2

if(n in lst):
    print("element found")
else:
    print("ele not found")