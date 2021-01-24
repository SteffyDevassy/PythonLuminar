n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
n3=int(input("Enter n3"))
if((n1>n2)&(n1>n3)):
    if(n2>n3):
        print("second largest",n2)
    else:
        print("second largest", n3)
elif((n2>n1)&(n2>n3)):
    if (n1 > n3):
        print("second largest", n1)
    else:
        print("second largest", n3)
elif((n3>n1)&(n3>n2)):
    if (n1 > n2):
        print("second largest", n1)
    else:
        print("second largest", n2)
else:
    print("no.s are equal")