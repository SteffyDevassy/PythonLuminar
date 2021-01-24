#read no=2
#min=49
#max=65
#result = 49(7^2) and 64(8^2)



#n=3,min=1,max=27
#1(1^3),8(2^3),27(3^3)

n=int(input("Enter power"))
min=int(input("Enter lower limit"))
max=int(input("Enter upper lmit"))
for i in range(1,(max+1)):
    if i**n in range(min,max+1):
        print(i,",",i,"^",n,"=",(i**n))