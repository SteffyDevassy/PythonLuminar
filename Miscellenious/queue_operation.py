size=int(input("Enter size of the queue"))
que=[]

global rear,front

n=1
def insert(value):
    global rear, front
    rear=front = -1

    if(front==0 and rear==size-1):
        print("Queue Overflow")
    else:
        if front==-1:
            front=0
        rear=rear+1
        que.insert(front,value)

        print(value ,"inserted")
def delet():
    global front,rear
    if front==-1:
        print("Queue Underflow")
    else:
        print(que[front])
        print("popped item is",que[front])
        front=front-1
def display():
    global front,rear
    if front==-1:
        print("Queue is empty")
    else:

        print("Elements in the Queue are: ")
        for q_item in que:
            print(q_item)


while(n!=0):
    option=int(input("Enter operation \n1.Insertion \n2.Deletion \n3.Display \n4.Exit\n"))
    if(option==1):
        value=int(input("Enter value to be inserted"))
        insert(value)
    elif option==2:
        delet()
    elif option==3:
        display()
    elif option==4:
        print("exit")
        exit(0)
    else:
        print("Invalid choice")

