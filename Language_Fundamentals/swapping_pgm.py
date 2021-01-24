n1=10
n2=20
print("values b4 swapping num1=",n1,"num2=",n2)
#method 1
t=n1
n1=n2
n2=t
print("values after swapping num1=",n1,"num2=",n2)



#method2
(n1,n2)=(n2,n1)

#method3
n1=n1+n2 #10+20=30
n2=n1-n2 #30-20=10
n1=n1-n2
