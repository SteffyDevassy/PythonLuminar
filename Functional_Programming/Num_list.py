#num<5= i-1
#num>5= i+1
first=[1,2,3,4,5,6,7]
data=[i-1 if i<5 else i+1 if i>5  else i for i in first]
print(data)

matrix=[[1,2,3],[4,5,6],[7,8,9]]
#flatten operation
flat=[j for i in matrix for j in i]
print(flat)