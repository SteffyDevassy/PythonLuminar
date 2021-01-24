first=[1,2,3]
second=[4,5,6]

#output1,4 1,5 ,1,6
pairs=[(i,j) for i in first for j in second]
print(pairs)

#squares
square=[i**2 for i in first]
print(square)


pair=[(i,j) for i**2 in first  for j**2 in second]
print(pair)