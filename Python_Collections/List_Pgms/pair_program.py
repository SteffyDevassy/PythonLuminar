lst=[1,2,3,4,6]
#1 2 3 4 6
#
low=0
upp=len(lst)-1
ele=8
while(low<=upp):
    total=lst[low]+lst[upp]
    if(ele<total):
        upp-=1
    elif(ele>total):
        low+=1
    elif(total==ele):
        print(ele,"=",lst[low],"",lst[upp])
        break
