n1=int(input("Enter no1"))
n2=int(input("Enter no2"))
try:
    res=n1/n2
    print(res)
except:
    n2=int(input("Enter no2"))
    try:
        res = n1 / n2
        print(res)
    except:
        n2 = int(input("Enter no2"))
        res = n1 / n2
        print(res)
finally:
    print("I have transaction")


