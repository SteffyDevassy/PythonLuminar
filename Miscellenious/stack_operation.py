size=int(input("Enter size of the stack"))
stk=[]

n=1
def push(value):
    global top
    top=-1
    if(top>size):
        print("Stack Overflow")
    else:
        stk.append(value)
        top+=1
        print(value ,"pushed")
def Pop():
    global top
    top=-1
    if stk==[]:
        print("Stack Underflow")
    else:
        item=stk.pop()
        top-=1
        print("popped item is",item)
def display():
    if stk==[]:
        print("Stack is empty")
    else:
        top = len(stk) - 1
        print("Elements in the stack are: ")
        for i in range(top, -1, -1):
            print(str(stk[i]))


while(n!=0):
    option=int(input("Enter operation \n1.Push \n2.Pop \n3.display \n4.Exit\n"))
    if(option==1):
        value=int(input("Enter value to be pushed"))
        push(value)
    elif option==2:
        Pop()
    elif option==3:
        display()
    elif option==4:
        print("exit")
        exit(0)
    else:
        print("Invalid choice")

