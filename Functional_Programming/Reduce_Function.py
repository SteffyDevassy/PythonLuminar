#Reduce function
#
from functools import *
lst=[1,2,3,4,5,6,7]
#sum
sum=reduce(lambda n1,n2:n1+n2,lst)
print(sum)


#min
minimum=reduce(lambda n1,n2:n1 if n1<n2 else n2,lst)
print(minimum)

#max
maximum=reduce(lambda n1,n2:n1 if n1>n2 else n2,lst)
print(maximum)

#find min of even no.s in list
e_min=reduce(lambda n1,n2:n1 if n1<n2 else n2,
             list(filter(lambda n1:n1%2==0,lst)))
print(e_min)