n1=int(input("Enter n1"))
n2=int(input("Enter n2"))
n3=int(input("Enter n3"))
if((n1>n2)&(n1>n3)):
    print("n1 is larger")
elif((n2>n1)&(n2>n3)):
    print("n2 is larger")
elif((n3>n1)&(n3>n2)):
    print("n3 is larger")
else:
    print("no.s are equal")