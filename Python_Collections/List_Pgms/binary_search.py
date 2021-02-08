lst=[5,7,6,1,2,3,4]
lst.sort()
print(lst)
low=0
upp=len(lst)-1
flag=0
ele=int(input("Enter ele to be searched"))
while(low<=upp):

    mid = (low + upp) // 2
    if(ele>lst[mid]):
        low=mid+1
        # upp=len(lst)-1
    elif(ele<lst[mid]):
        # low=0
        upp=mid-1
    elif(ele==lst[mid]):
        flag+=1
        break
if(flag==0):
    print("no ele")
else:
    print("ele found")


