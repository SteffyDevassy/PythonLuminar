lst=[5,4,3,2] #[9,10,11,12]
#lst=[5,6,3,4]  [13,12,15,14]
tot=sum(lst)
out=[]
for num in lst:
    out.append(tot-num)
print(out)