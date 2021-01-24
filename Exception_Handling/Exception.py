#runtime error /abnormal code that disrupt normal execution

n1=int(input("Enter no1"))
n2=int(input("Enter no2"))

try:
    res=n1/n2
    print(res)
except Exception as e:
    print("error")
    print(e.args)

#try-abnormal code
#except--exception handling code
#finally--cleanup code