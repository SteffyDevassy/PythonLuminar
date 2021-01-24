# map()
# filter()
# reduce()
lst=[10,11,12,13,14,15]

#square of each word
#  map(function,iterables)

sqaures=list(map(lambda num:num**2,lst))
cube=list(map(lambda num:num**3,lst))
print(sqaures,cube)

#find even no.s
#Filter
even=list(filter(lambda num:num%2==0,lst))
print(even)







